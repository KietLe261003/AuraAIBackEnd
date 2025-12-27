from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import uuid

from app.models.task import Task
from app.models.task_depends_on import TaskDependsOn
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    
    @staticmethod
    async def generate_name() -> str:
        return f"TASK-{uuid.uuid4().hex[:8].upper()}"
    
    @staticmethod
    async def create(db: AsyncSession, task_data: TaskCreate) -> Task:
        name = await TaskService.generate_name()
        
        # Extract depends_on data
        depends_on_data = task_data.depends_on or []
        task_dict = task_data.model_dump(exclude={"depends_on"})
        
        task = Task(name=name, **task_dict)
        db.add(task)
        await db.flush()
        
        # Create task dependencies if provided
        if depends_on_data:
            for idx, dep_data in enumerate(depends_on_data):
                dep_dict = dep_data.model_dump()
                dep_dict["name"] = f"{name}-DEP-{uuid.uuid4().hex[:6].upper()}"
                dep_dict["parent"] = name
                dep_dict["parenttype"] = "Task"
                dep_dict["parentfield"] = "depends_on"
                dep_dict["idx"] = idx + 1
                task_dep = TaskDependsOn(**dep_dict)
                db.add(task_dep)
        stmt = (
            select(Task)
            .options(selectinload(Task.depends_on)) # Nạp sẵn quan hệ phụ thuộc
            .filter(Task.name == name)
        )
        result = await db.execute(stmt)
        return result.scalar_one()
    @staticmethod
    async def create_multiple(db: AsyncSession, tasks_data: List[TaskCreate]) -> List[Task]:
        tasks = []
        for task_data in tasks_data:
            task = await TaskService.create(db, task_data)
            tasks.append(task)
        return tasks

    @staticmethod
    async def get_by_name(db: AsyncSession, name: str) -> Optional[Task]:
        query = select(Task).options(
            selectinload(Task.depends_on)
        ).where(Task.name == name)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_all(
        db: AsyncSession, 
        skip: int = 0, 
        limit: int = 100,
        project: Optional[str] = None,
        status: Optional[str] = None,
        assigned_to: Optional[str] = None
    ) -> List[Task]:
        query = select(Task).options(
            selectinload(Task.depends_on)
        )
        
        if project:
            query = query.where(Task.project == project)
        if status:
            query = query.where(Task.status == status)
        if assigned_to:
            query = query.where(Task.assigned_to == assigned_to)
            
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def update(db: AsyncSession, name: str, task_data: TaskUpdate) -> Optional[Task]:
        task = await TaskService.get_by_name(db, name)
        if not task:
            return None
        
        update_data = task_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)
        
        await db.commit()
        await db.refresh(task)
        return task
    
    @staticmethod
    async def delete(db: AsyncSession, name: str) -> bool:
        task = await TaskService.get_by_name(db, name)
        if not task:
            return False
        
        await db.delete(task)
        await db.commit()
        return True
    
    @staticmethod
    async def get_by_project(db: AsyncSession, project_name: str) -> List[Task]:
        query = select(Task).options(
            selectinload(Task.depends_on)
        ).where(Task.project == project_name)
        result = await db.execute(query)
        return result.scalars().all()
