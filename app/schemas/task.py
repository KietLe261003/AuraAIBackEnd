from pydantic import BaseModel
from typing import Optional, List, Literal
from datetime import datetime
from app.schemas.task_depends_on import TaskDependsOnResponse, TaskDependsOnCreate


class TaskBase(BaseModel):
    subject: str
    project: Optional[str] = None
    issue: Optional[str] = None
    type: Optional[str] = None
    color: Optional[str] = None
    is_group: Optional[int] = 0
    is_template: Optional[int] = 0
    status: Optional[Literal["Open", "Working", "Pending Review", "Overdue", "Template", "Completed", "Cancelled"]] = "Open"
    priority: Optional[Literal["Low", "Medium", "High", "Urgent"]] = "Medium"
    is_important: Optional[int] = 0
    task_weight: Optional[float] = None
    parent_task: Optional[str] = None
    completed_by: Optional[str] = None
    completed_on: Optional[datetime] = None
    assigned_to: Optional[str] = None
    exp_start_date: Optional[datetime] = None
    expected_time: Optional[float] = None
    start: Optional[int] = None
    exp_end_date: Optional[datetime] = None
    progress: Optional[float] = 0
    duration: Optional[int] = None
    is_milestone: Optional[int] = 0
    description: Optional[str] = None
    depends_on_tasks: Optional[str] = None
    review_date: Optional[datetime] = None
    closing_date: Optional[datetime] = None
    department: Optional[str] = None
    company: Optional[str] = None
    template_task: Optional[str] = None


class TaskCreate(TaskBase):
    owner: str
    depends_on: Optional[List[TaskDependsOnCreate]] = None


class TaskUpdate(BaseModel):
    subject: Optional[str] = None
    project: Optional[str] = None
    issue: Optional[str] = None
    type: Optional[str] = None
    color: Optional[str] = None
    is_group: Optional[int] = None
    is_template: Optional[int] = None
    status: Optional[Literal["Open", "Working", "Pending Review", "Overdue", "Template", "Completed", "Cancelled"]] = None
    priority: Optional[Literal["Low", "Medium", "High", "Urgent"]] = None
    is_important: Optional[int] = None
    task_weight: Optional[float] = None
    parent_task: Optional[str] = None
    completed_by: Optional[str] = None
    completed_on: Optional[datetime] = None
    assigned_to: Optional[str] = None
    exp_start_date: Optional[datetime] = None
    expected_time: Optional[float] = None
    exp_end_date: Optional[datetime] = None
    progress: Optional[float] = None
    duration: Optional[int] = None
    is_milestone: Optional[int] = None
    description: Optional[str] = None
    depends_on_tasks: Optional[str] = None
    review_date: Optional[datetime] = None
    closing_date: Optional[datetime] = None
    department: Optional[str] = None
    company: Optional[str] = None
    modified_by: Optional[str] = None


class TaskResponse(TaskBase):
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
    act_start_date: Optional[datetime] = None
    actual_time: Optional[float] = None
    act_end_date: Optional[datetime] = None
    total_costing_amount: Optional[float] = None
    total_expense_claim: Optional[float] = None
    total_billing_amount: Optional[float] = None
    lft: Optional[int] = None
    rgt: Optional[int] = None
    old_parent: Optional[str] = None
    depends_on: Optional[List[TaskDependsOnResponse]] = []
    
    class Config:
        from_attributes = True
