from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.schemas.response import APIResponse
from app.services.task_service import TaskService

router = APIRouter()


@router.post("/", response_model=APIResponse[TaskResponse], status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new task"""
    task = await TaskService.create(db, task_data)
    return APIResponse(
        success=True,
        message="Task created successfully",
        data=task
    )

@router.post("/multiple", response_model=APIResponse[List[TaskResponse]], status_code=status.HTTP_201_CREATED)
async def create_multiple_tasks(
    tasks_data: List[TaskCreate],
    db: AsyncSession = Depends(get_db)
):
    """Create multiple tasks"""
    tasks = await TaskService.create_multiple(db, tasks_data)
    return APIResponse(
        success=True,
        message="Tasks created successfully",
        data=tasks
    )


@router.get("/", response_model=APIResponse[List[TaskResponse]])
async def get_tasks(
    skip: int = 0,
    limit: int = 100,
    project: Optional[str] = None,
    status: Optional[str] = None,
    assigned_to: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Get all tasks with optional filters"""
    tasks = await TaskService.get_all(
        db, skip=skip, limit=limit, 
        project=project, status=status, assigned_to=assigned_to
    )
    return APIResponse(
        success=True,
        message="Tasks retrieved successfully",
        data=tasks
    )


@router.get("/{name}", response_model=APIResponse[TaskResponse])
async def get_task(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific task by name"""
    task = await TaskService.get_by_name(db, name)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Task retrieved successfully",
        data=task
    )


@router.put("/{name}", response_model=APIResponse[TaskResponse])
async def update_task(
    name: str,
    task_data: TaskUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a task"""
    task = await TaskService.update(db, name, task_data)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Task updated successfully",
        data=task
    )


@router.delete("/{name}", response_model=APIResponse)
async def delete_task(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    """Delete a task"""
    deleted = await TaskService.delete(db, name)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with name '{name}' not found"
        )
    return APIResponse(
        success=True,
        message="Task deleted successfully",
        data=None
    )


@router.get("/project/{project_name}", response_model=APIResponse[List[TaskResponse]])
async def get_tasks_by_project(
    project_name: str,
    db: AsyncSession = Depends(get_db)
):
    """Get all tasks for a specific project"""
    tasks = await TaskService.get_by_project(db, project_name)
    return APIResponse(
        success=True,
        message="Tasks retrieved successfully",
        data=tasks
    )
