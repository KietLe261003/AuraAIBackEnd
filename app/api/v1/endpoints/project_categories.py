from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.project_category import ProjectCategoryCreate, ProjectCategoryUpdate, ProjectCategoryResponse
from app.schemas.response import APIResponse
from app.services.project_category_service import ProjectCategoryService

router = APIRouter()


@router.post("/", response_model=APIResponse[ProjectCategoryResponse], status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data: ProjectCategoryCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new project category"""
    category = await ProjectCategoryService.create(db, category_data)
    return APIResponse(
        success=True,
        message="Project category created successfully",
        data=category
    )


@router.get("/", response_model=APIResponse[List[ProjectCategoryResponse]])
async def get_categories(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all project categories"""
    categories = await ProjectCategoryService.get_all(db, skip=skip, limit=limit)
    return APIResponse(
        success=True,
        message="Project categories retrieved successfully",
        data=categories
    )


@router.get("/{name}", response_model=APIResponse[ProjectCategoryResponse])
async def get_category(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific project category by name"""
    category = await ProjectCategoryService.get_by_name(db, name)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project Category with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project category retrieved successfully",
        data=category
    )


@router.put("/{name}", response_model=APIResponse[ProjectCategoryResponse])
async def update_category(
    name: str,
    category_data: ProjectCategoryUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a project category"""
    category = await ProjectCategoryService.update(db, name, category_data)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project Category with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project category updated successfully",
        data=category
    )


@router.delete("/{name}", response_model=APIResponse)
async def delete_category(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Delete a project category"""
    deleted = await ProjectCategoryService.delete(db, name)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project Category with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Project category deleted successfully",
        data=None
    )
