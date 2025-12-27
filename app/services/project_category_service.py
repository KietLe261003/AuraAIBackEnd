from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid

from app.models.project_category import ProjectCategory
from app.schemas.project_category import ProjectCategoryCreate, ProjectCategoryUpdate


class ProjectCategoryService:
    
    @staticmethod
    async def generate_name() -> str:
        return f"PCAT-{uuid.uuid4().hex[:8].upper()}"
    
    @staticmethod
    async def create(db: AsyncSession, category_data: ProjectCategoryCreate) -> ProjectCategory:
        name = await ProjectCategoryService.generate_name()
        category_dict = category_data.model_dump()
        
        category = ProjectCategory(name=name, **category_dict)
        db.add(category)
        await db.commit()
        await db.refresh(category)
        return category
    
    @staticmethod
    async def get_by_name(db: AsyncSession, name: str) -> Optional[ProjectCategory]:
        query = select(ProjectCategory).where(ProjectCategory.name == name)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_all(
        db: AsyncSession, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[ProjectCategory]:
        query = select(ProjectCategory).offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def update(db: AsyncSession, name: str, category_data: ProjectCategoryUpdate) -> Optional[ProjectCategory]:
        category = await ProjectCategoryService.get_by_name(db, name)
        if not category:
            return None
        
        update_data = category_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(category, field, value)
        
        await db.commit()
        await db.refresh(category)
        return category
    
    @staticmethod
    async def delete(db: AsyncSession, name: str) -> bool:
        category = await ProjectCategoryService.get_by_name(db, name)
        if not category:
            return False
        
        await db.delete(category)
        await db.commit()
        return True
