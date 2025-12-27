from typing import Generic, TypeVar, Optional, List, Any
from pydantic import BaseModel

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    """Standard API Response Wrapper"""
    success: bool = True
    message: str = "Success"
    data: Optional[T] = None
    
    class Config:
        from_attributes = True


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated API Response Wrapper"""
    success: bool = True
    message: str = "Success"
    data: Optional[List[T]] = None
    total: Optional[int] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    
    class Config:
        from_attributes = True


class ErrorResponse(BaseModel):
    """Error Response"""
    success: bool = False
    message: str
    error_code: Optional[str] = None
    details: Optional[Any] = None
