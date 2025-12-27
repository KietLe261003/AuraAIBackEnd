from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid

from app.models.project_user import ProjectUser
from app.schemas.project_user import ProjectUserCreate, ProjectUserUpdate


class ProjectUserService:
    
    @staticmethod
    async def generate_name() -> str:
        return f"PUSER-{uuid.uuid4().hex[:8].upper()}"
    
    @staticmethod
    async def create(db: AsyncSession, user_data: ProjectUserCreate) -> ProjectUser:
        name = await ProjectUserService.generate_name()
        user_dict = user_data.model_dump()
        
        user = ProjectUser(name=name, **user_dict)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    
    @staticmethod
    async def create_multiple(db: AsyncSession, users_data: List[ProjectUserCreate]) -> List[ProjectUser]:
        users = []
        for user_data in users_data:
            name = await ProjectUserService.generate_name()
            user_dict = user_data.model_dump()
            user = ProjectUser(name=name, **user_dict)
            db.add(user)
            users.append(user)
        
        await db.commit()
        for user in users:
            await db.refresh(user)
        return users
    
    @staticmethod
    async def get_by_name(db: AsyncSession, name: str) -> Optional[ProjectUser]:
        query = select(ProjectUser).where(ProjectUser.name == name)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_all(
        db: AsyncSession, 
        skip: int = 0, 
        limit: int = 100,
        project: Optional[str] = None
    ) -> List[ProjectUser]:
        query = select(ProjectUser)
        
        if project:
            query = query.where(ProjectUser.parent == project)
            
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def update(db: AsyncSession, name: str, user_data: ProjectUserUpdate) -> Optional[ProjectUser]:
        user = await ProjectUserService.get_by_name(db, name)
        if not user:
            return None
        
        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        
        await db.commit()
        await db.refresh(user)
        return user
    
    @staticmethod
    async def delete(db: AsyncSession, name: str) -> bool:
        user = await ProjectUserService.get_by_name(db, name)
        if not user:
            return False
        
        await db.delete(user)
        await db.commit()
        return True
    
    @staticmethod
    async def get_by_project(db: AsyncSession, project_name: str) -> List[ProjectUser]:
        query = select(ProjectUser).where(ProjectUser.parent == project_name)
        result = await db.execute(query)
        return result.scalars().all()
