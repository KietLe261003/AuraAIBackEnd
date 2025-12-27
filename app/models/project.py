from sqlalchemy import Column, String, Integer, Float, Text, DateTime, Enum, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base
import enum


class ProjectStatus(str, enum.Enum):
    OPEN = "Open"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class IsActive(str, enum.Enum):
    YES = "Yes"
    NO = "No"


class PercentCompleteMethod(str, enum.Enum):
    MANUAL = "Manual"
    TASK_COMPLETION = "Task Completion"
    TASK_PROGRESS = "Task Progress"
    TASK_WEIGHT = "Task Weight"


class Priority(str, enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Frequency(str, enum.Enum):
    HOURLY = "Hourly"
    TWICE_DAILY = "Twice Daily"
    DAILY = "Daily"
    WEEKLY = "Weekly"


class DayToSend(str, enum.Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class Project(Base):
    __tablename__ = "projects"
    
    name = Column(String(255), primary_key=True, index=True)
    creation = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())
    owner = Column(String(255), nullable=False)
    modified_by = Column(String(255))
    docstatus = Column(Integer, default=0)  # 0, 1, 2
    parent = Column(String(255), nullable=True)
    parentfield = Column(String(255), nullable=True)
    parenttype = Column(String(255), nullable=True)
    idx = Column(Integer, nullable=True)
    
    # Project specific fields
    naming_series = Column(String(50), default="PROJ-.####")
    project_name = Column(String(255), nullable=False)
    status = Column(String(50), default="Open")
    project_type = Column(String(255), nullable=True)
    category = Column(String(255), ForeignKey("project_categories.name"), nullable=True)
    is_active = Column(String(10), default="Yes")
    percent_complete_method = Column(String(50), default="Manual")
    percent_complete = Column(Float, default=0)
    project_template = Column(String(255), nullable=True)
    expected_start_date = Column(DateTime(timezone=True), nullable=True)
    expected_end_date = Column(DateTime(timezone=True), nullable=True)
    priority = Column(String(20), default="Medium")
    department = Column(String(255), nullable=True)
    team = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    actual_start_date = Column(DateTime(timezone=True), nullable=True)
    actual_time = Column(Float, nullable=True)
    actual_end_date = Column(DateTime(timezone=True), nullable=True)
    estimated_costing = Column(Float, nullable=True)
    total_costing_amount = Column(Float, nullable=True)
    total_purchase_cost = Column(Float, nullable=True)
    total_sales_amount = Column(Float, nullable=True)
    total_billable_amount = Column(Float, nullable=True)
    total_billed_amount = Column(Float, nullable=True)
    total_consumed_material_cost = Column(Float, nullable=True)
    cost_center = Column(String(255), nullable=True)
    gross_margin = Column(Float, nullable=True)
    per_gross_margin = Column(Float, nullable=True)
    collect_progress = Column(Integer, default=0)
    holiday_list = Column(String(255), nullable=True)
    frequency = Column(String(50), nullable=True)
    from_time = Column(String(20), nullable=True)
    to_time = Column(String(20), nullable=True)
    first_email = Column(String(20), nullable=True)
    second_email = Column(String(20), nullable=True)
    daily_time_to_send = Column(String(20), nullable=True)
    day_to_send = Column(String(20), nullable=True)
    weekly_time_to_send = Column(String(20), nullable=True)
    subject = Column(String(255), nullable=True)
    message = Column(Text, nullable=True)
    rd_template = Column(String(255), nullable=True)
    tasks_completed_this_week = Column(Integer, nullable=True)
    department_migrated = Column(String(255), nullable=True)
    
    # Relationships
    category_details = relationship("ProjectCategory", back_populates="projects")
    users = relationship("ProjectUser", back_populates="project", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="project_rel", cascade="all, delete-orphan")
