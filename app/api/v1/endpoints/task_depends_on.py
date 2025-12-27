from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.task_depends_on import TaskDependsOnCreate, TaskDependsOnUpdate, TaskDependsOnResponse
from app.schemas.response import APIResponse
from app.services.task_depends_on_service import TaskDependsOnService

router = APIRouter()


@router.post("/", response_model=APIResponse[TaskDependsOnResponse], status_code=status.HTTP_201_CREATED)
async def create_task_dependency(
    dep_data: TaskDependsOnCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new task dependency"""
    dependency = await TaskDependsOnService.create(db, dep_data)
    return APIResponse(
        success=True,
        message="Task dependency created successfully",
        data=dependency
    )


@router.get("/", response_model=APIResponse[List[TaskDependsOnResponse]])
async def get_task_dependencies(
    skip: int = 0,
    limit: int = 100,
    task: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Get all task dependencies with optional task filter"""
    dependencies = await TaskDependsOnService.get_all(db, skip=skip, limit=limit, task=task)
    return APIResponse(
        success=True,
        message="Task dependencies retrieved successfully",
        data=dependencies
    )


@router.get("/{name}", response_model=APIResponse[TaskDependsOnResponse])
async def get_task_dependency(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific task dependency by name"""
    dependency = await TaskDependsOnService.get_by_name(db, name)
    if not dependency:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task Dependency with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Task dependency retrieved successfully",
        data=dependency
    )


@router.put("/{name}", response_model=APIResponse[TaskDependsOnResponse])
async def update_task_dependency(
    name: str,
    dep_data: TaskDependsOnUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a task dependency"""
    dependency = await TaskDependsOnService.update(db, name, dep_data)
    if not dependency:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task Dependency with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Task dependency updated successfully",
        data=dependency
    )


@router.delete("/{name}", response_model=APIResponse)
async def delete_task_dependency(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Delete a task dependency"""
    deleted = await TaskDependsOnService.delete(db, name)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task Dependency with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Task dependency deleted successfully",
        data=None
    )


@router.get("/task/{task_name}", response_model=APIResponse[List[TaskDependsOnResponse]])
async def get_dependencies_by_task(
    task_name: str,
    db: AsyncSession = Depends(get_db)
):
    """Get all dependencies for a specific task"""
    dependencies = await TaskDependsOnService.get_by_task(db, task_name)
    return APIResponse(
        success=True,
        message="Task dependencies retrieved successfully",
        data=dependencies
    )
