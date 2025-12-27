from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProjectCategoryBase(BaseModel):
    category_name: str
    description: Optional[str] = None


class ProjectCategoryCreate(ProjectCategoryBase):
    owner: str


class ProjectCategoryUpdate(BaseModel):
    category_name: Optional[str] = None
    description: Optional[str] = None
    modified_by: Optional[str] = None


class ProjectCategoryResponse(ProjectCategoryBase):
    name: str
    creation: Optional[datetime] = None
    modified: Optional[datetime] = None
    owner: str
    modified_by: Optional[str] = None
    docstatus: int = 0
    
    class Config:
        from_attributes = True
