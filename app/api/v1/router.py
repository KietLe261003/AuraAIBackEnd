from fastapi import APIRouter
from app.api.v1.endpoints import projects, tasks, project_categories, project_users, task_depends_on

api_router = APIRouter()

api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(project_categories.router, prefix="/project-categories", tags=["project-categories"])
api_router.include_router(project_users.router, prefix="/project-users", tags=["project-users"])
api_router.include_router(task_depends_on.router, prefix="/task-depends-on", tags=["task-depends-on"])
