from fastapi import APIRouter, Depends
from app.api.v1.endpoints import projects, tasks, project_categories, project_users, task_depends_on, auth
from app.api.deps import get_current_user

api_router = APIRouter()

# Public routes (no authentication required)
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])

# Protected routes (authentication required)
protected_router = APIRouter(dependencies=[Depends(get_current_user)])
protected_router.include_router(projects.router, prefix="/projects", tags=["projects"])
protected_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
protected_router.include_router(project_categories.router, prefix="/project-categories", tags=["project-categories"])
protected_router.include_router(project_users.router, prefix="/project-users", tags=["project-users"])
protected_router.include_router(task_depends_on.router, prefix="/task-depends-on", tags=["task-depends-on"])

api_router.include_router(protected_router)
