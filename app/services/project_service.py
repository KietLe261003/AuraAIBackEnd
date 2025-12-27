from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload
import uuid

from app.models.project import Project
from app.models.project_user import ProjectUser
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:
    
    @staticmethod
    async def generate_name() -> str:
        return f"PROJ-{uuid.uuid4().hex[:8].upper()}"
    
    @staticmethod
    async def create(db: AsyncSession, project_data: ProjectCreate) -> Project:
        name = await ProjectService.generate_name()
        
        # Extract users data
        users_data = project_data.users
        project_dict = project_data.model_dump(exclude={"users"})
        
        project = Project(name=name, **project_dict)
        db.add(project)
        await db.flush()
        
        # Create project users if provided
        if users_data:
            for idx, user_data in enumerate(users_data):
                user_dict = user_data.model_dump()
                user_dict["name"] = f"{name}-USER-{uuid.uuid4().hex[:6].upper()}"
                user_dict["parent"] = name
                user_dict["parenttype"] = "Project"
                user_dict["parentfield"] = "users"
                user_dict["idx"] = idx + 1
                # Set owner from project if not provided
                if not user_dict.get("owner"):
                    user_dict["owner"] = project_dict["owner"]
                project_user = ProjectUser(**user_dict)
                db.add(project_user)
        
        await db.commit()
        
        # Reload with relationships
        return await ProjectService.get_by_name(db, project.name)
    
    @staticmethod
    async def get_by_name(db: AsyncSession, name: str) -> Optional[Project]:
        query = select(Project).options(
            selectinload(Project.users),
            selectinload(Project.category_details)
        ).where(Project.name == name)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_all(
        db: AsyncSession, 
        skip: int = 0, 
        limit: int = 100,
        status: Optional[str] = None,
        company: Optional[str] = None
    ) -> List[Project]:
        query = select(Project).options(
            selectinload(Project.users),
            selectinload(Project.category_details)
        )
        
        if status:
            query = query.where(Project.status == status)
        if company:
            query = query.where(Project.company == company)
            
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def update(db: AsyncSession, name: str, project_data: ProjectUpdate) -> Optional[Project]:
        project = await ProjectService.get_by_name(db, name)
        if not project:
            return None
        
        update_data = project_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(project, field, value)
        
        await db.commit()
        
        # Reload with relationships
        return await ProjectService.get_by_name(db, name)
    
    @staticmethod
    async def delete(db: AsyncSession, name: str) -> bool:
        project = await ProjectService.get_by_name(db, name)
        if not project:
            return False
        
        await db.delete(project)
        await db.commit()
        return True
