from pydantic import BaseModel
from typing import Optional, List, Literal
from datetime import datetime
from app.schemas.project_user import ProjectUserResponse, ProjectUserCreate
from app.schemas.project_category import ProjectCategoryResponse


class ProjectBase(BaseModel):
    project_name: str
    naming_series: str = "PROJ-.####"
    status: Optional[Literal["Open", "Completed", "Cancelled"]] = "Open"
    project_type: Optional[str] = None
    category: Optional[str] = None
    is_active: Optional[Literal["Yes", "No"]] = "Yes"
    percent_complete_method: Optional[Literal["Manual", "Task Completion", "Task Progress", "Task Weight"]] = "Manual"
    percent_complete: Optional[float] = 0
    project_template: Optional[str] = None
    expected_start_date: Optional[datetime] = None
    expected_end_date: Optional[datetime] = None
    priority: Optional[Literal["Low", "Medium", "High"]] = "Medium"
    department: Optional[str] = None
    team: Optional[str] = None
    notes: Optional[str] = None
    estimated_costing: Optional[float] = None
    cost_center: Optional[str] = None
    collect_progress: Optional[int] = 0
    holiday_list: Optional[str] = None
    frequency: Optional[Literal["Hourly", "Twice Daily", "Daily", "Weekly"]] = None
    from_time: Optional[str] = None
    to_time: Optional[str] = None
    first_email: Optional[str] = None
    second_email: Optional[str] = None
    daily_time_to_send: Optional[str] = None
    day_to_send: Optional[Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]] = None
    weekly_time_to_send: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    rd_template: Optional[str] = None
    tasks_completed_this_week: Optional[int] = None
    department_migrated: Optional[str] = None


class ProjectCreate(ProjectBase):
    owner: str
    users: Optional[List[ProjectUserCreate]] = None


class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    status: Optional[Literal["Open", "Completed", "Cancelled"]] = None
    project_type: Optional[str] = None
    category: Optional[str] = None
    is_active: Optional[Literal["Yes", "No"]] = None
    percent_complete_method: Optional[Literal["Manual", "Task Completion", "Task Progress", "Task Weight"]] = None
    percent_complete: Optional[float] = None
    project_template: Optional[str] = None
    expected_start_date: Optional[datetime] = None
    expected_end_date: Optional[datetime] = None
    priority: Optional[Literal["Low", "Medium", "High"]] = None
    department: Optional[str] = None
    team: Optional[str] = None
    customer: Optional[str] = None
    sales_order: Optional[str] = None
    notes: Optional[str] = None
    estimated_costing: Optional[float] = None
    cost_center: Optional[str] = None
    collect_progress: Optional[int] = None
    holiday_list: Optional[str] = None
    frequency: Optional[Literal["Hourly", "Twice Daily", "Daily", "Weekly"]] = None
    modified_by: Optional[str] = None


class ProjectResponse(ProjectBase):
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
    actual_start_date: Optional[datetime] = None
    actual_time: Optional[float] = None
    actual_end_date: Optional[datetime] = None
    total_costing_amount: Optional[float] = None
    total_purchase_cost: Optional[float] = None
    total_sales_amount: Optional[float] = None
    total_billable_amount: Optional[float] = None
    total_billed_amount: Optional[float] = None
    total_consumed_material_cost: Optional[float] = None
    gross_margin: Optional[float] = None
    per_gross_margin: Optional[float] = None
    users: Optional[List[ProjectUserResponse]] = None
    category_details: Optional[ProjectCategoryResponse] = None
    
    class Config:
        from_attributes = True
