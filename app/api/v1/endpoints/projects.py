from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.schemas.response import APIResponse
from app.services.project_service import ProjectService

router = APIRouter()

@router.post("/", response_model=APIResponse[ProjectResponse], status_code=status.HTTP_201_CREATED)
async def create_project(
    project_data: ProjectCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new project"""
    project = await ProjectService.create(db, project_data)
    return APIResponse(
        success=True,
        message="Project created successfully",
        data=project
    )


@router.get("/", response_model=APIResponse[List[ProjectResponse]])
async def get_projects(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    company: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Get all projects with optional filters"""
    projects = await ProjectService.get_all(db, skip=skip, limit=limit, status=status, company=company)
    return APIResponse(
        success=True,
        message="Projects retrieved successfully",
        data=projects
    )


@router.get("/{name}", response_model=APIResponse[ProjectResponse])
async def get_project(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific project by name"""
    project = await ProjectService.get_by_name(db, name)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project retrieved successfully",
        data=project
    )


@router.put("/{name}", response_model=APIResponse[ProjectResponse])
async def update_project(
    name: str,
    project_data: ProjectUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a project"""
    project = await ProjectService.update(db, name, project_data)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project updated successfully",
        data=project
    )


@router.delete("/{name}", response_model=APIResponse)
async def delete_project(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Delete a project"""
    deleted = await ProjectService.delete(db, name)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project deleted successfully",
        data=None
    )
