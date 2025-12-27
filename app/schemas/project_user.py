from pydantic import BaseModel
from typing import Optional, List, Literal
from datetime import datetime


class ProjectUserBase(BaseModel):
    user: Optional[str] = None
    role: Optional[str] = None
    email: Optional[str] = None
    view_attachments: Optional[int] = 1
    welcome_email_sent: Optional[int] = 0


class ProjectUserCreate(ProjectUserBase):
    owner: Optional[str] = None
    parent: Optional[str] = None


class ProjectUserUpdate(BaseModel):
    user: Optional[str] = None
    role: Optional[str] = None
    email: Optional[str] = None
    view_attachments: Optional[int] = None
    welcome_email_sent: Optional[int] = None
    modified_by: Optional[str] = None


class ProjectUserResponse(ProjectUserBase):
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
