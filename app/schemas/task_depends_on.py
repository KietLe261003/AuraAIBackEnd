from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskDependsOnBase(BaseModel):
    task: Optional[str] = None
    subject: Optional[str] = None
    project: Optional[str] = None


class TaskDependsOnCreate(TaskDependsOnBase):
    owner: str
    parent: Optional[str] = None


class TaskDependsOnUpdate(BaseModel):
    task: Optional[str] = None
    subject: Optional[str] = None
    project: Optional[str] = None
    modified_by: Optional[str] = None


class TaskDependsOnResponse(TaskDependsOnBase):
    name: str
    creation: Optional[datetime] = None
    modified: Optional[datetime] = None
    owner: str
    modified_by: Optional[str] = None
    docstatus: int = 0
    parent: Optional[str] = None
    parentfield: Optional[str] = None
    parenttype: Optional[str] = None
    idx: Optional[int] = None
    
    class Config:
        from_attributes = True
