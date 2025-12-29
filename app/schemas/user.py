from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
class User(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    is_admin: bool
    created_at: datetime
    updated_at: datetime

class ResponseUser(BaseModel):
    user: User
    access_token: str
    expires_in: int
class UserOut(BaseModel):
    id: int
    email: str
    full_name: Optional[str] = None
    is_admin: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
