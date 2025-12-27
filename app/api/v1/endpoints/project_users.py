from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.project_user import ProjectUserCreate, ProjectUserUpdate, ProjectUserResponse
from app.schemas.response import APIResponse
from app.services.project_user_service import ProjectUserService

router = APIRouter()


@router.post("/", response_model=APIResponse[ProjectUserResponse], status_code=status.HTTP_201_CREATED)
async def create_project_user(
    user_data: ProjectUserCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new project user"""
    user = await ProjectUserService.create(db, user_data)
    return APIResponse(
        success=True,
        message="Project user created successfully",
        data=user
    )

@router.post("/create-multiple", response_model=APIResponse[List[ProjectUserResponse]], status_code=status.HTTP_201_CREATED)
async def create_multiple_project_users(
    users_data: List[ProjectUserCreate],
    db: AsyncSession = Depends(get_db)
):
    """Create multiple project users"""
    users = await ProjectUserService.create_multiple(db, users_data)
    return APIResponse(
        success=True,
        message="Project users created successfully",
        data=users
    )

@router.get("/", response_model=APIResponse[List[ProjectUserResponse]])
async def get_project_users(
    skip: int = 0,
    limit: int = 100,
    project: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Get all project users with optional project filter"""
    users = await ProjectUserService.get_all(db, skip=skip, limit=limit, project=project)
    return APIResponse(
        success=True,
        message="Project users retrieved successfully",
        data=users
    )


@router.get("/{name}", response_model=APIResponse[ProjectUserResponse])
async def get_project_user(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific project user by name"""
    user = await ProjectUserService.get_by_name(db, name)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project User with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project user retrieved successfully",
        data=user
    )


@router.put("/{name}", response_model=APIResponse[ProjectUserResponse])
async def update_project_user(
    name: str,
    user_data: ProjectUserUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a project user"""
    user = await ProjectUserService.update(db, name, user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project User with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project user updated successfully",
        data=user
    )


@router.delete("/{name}", response_model=APIResponse)
async def delete_project_user(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Delete a project user"""
    deleted = await ProjectUserService.delete(db, name)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project User with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project user deleted successfully",
        data=None
    )


@router.get("/project/{project_name}", response_model=APIResponse[List[ProjectUserResponse]])
async def get_users_by_project(
    project_name: str,
    db: AsyncSession = Depends(get_db)
):
    """Get all users for a specific project"""
    users = await ProjectUserService.get_by_project(db, project_name)
    return APIResponse(
        success=True,
        message="Project users retrieved successfully",
        data=users
    )
