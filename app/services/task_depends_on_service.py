from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid

from app.models.task_depends_on import TaskDependsOn
from app.schemas.task_depends_on import TaskDependsOnCreate, TaskDependsOnUpdate


class TaskDependsOnService:
    
    @staticmethod
    async def generate_name() -> str:
        return f"TDEP-{uuid.uuid4().hex[:8].upper()}"
    
    @staticmethod
    async def create(db: AsyncSession, dep_data: TaskDependsOnCreate) -> TaskDependsOn:
        name = await TaskDependsOnService.generate_name()
        dep_dict = dep_data.model_dump()
        
        dependency = TaskDependsOn(name=name, **dep_dict)
        db.add(dependency)
        await db.commit()
        await db.refresh(dependency)
        return dependency
    
    @staticmethod
    async def get_by_name(db: AsyncSession, name: str) -> Optional[TaskDependsOn]:
        query = select(TaskDependsOn).where(TaskDependsOn.name == name)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_all(
        db: AsyncSession, 
        skip: int = 0, 
        limit: int = 100,
        task: Optional[str] = None
    ) -> List[TaskDependsOn]:
        query = select(TaskDependsOn)
        
        if task:
            query = query.where(TaskDependsOn.parent == task)
            
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def update(db: AsyncSession, name: str, dep_data: TaskDependsOnUpdate) -> Optional[TaskDependsOn]:
        dependency = await TaskDependsOnService.get_by_name(db, name)
        if not dependency:
            return None
        
        update_data = dep_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(dependency, field, value)
        
        await db.commit()
        await db.refresh(dependency)
        return dependency
    
    @staticmethod
    async def delete(db: AsyncSession, name: str) -> bool:
        dependency = await TaskDependsOnService.get_by_name(db, name)
        if not dependency:
            return False
        
        await db.delete(dependency)
        await db.commit()
        return True
    
    @staticmethod
    async def get_by_task(db: AsyncSession, task_name: str) -> List[TaskDependsOn]:
        query = select(TaskDependsOn).where(TaskDependsOn.parent == task_name)
        result = await db.execute(query)
        return result.scalars().all()
