from sqlalchemy import Column, String, Integer, Float, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base
import enum


class TaskStatus(str, enum.Enum):
    OPEN = "Open"
    WORKING = "Working"
    PENDING_REVIEW = "Pending Review"
    OVERDUE = "Overdue"
    TEMPLATE = "Template"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class TaskPriority(str, enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    URGENT = "Urgent"


class Task(Base):
    __tablename__ = "tasks"
    
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
    
    # Task specific fields
    subject = Column(String(255), nullable=False)
    project = Column(String(255), ForeignKey("projects.name"), nullable=True)
    issue = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    color = Column(String(50), nullable=True)
    is_group = Column(Integer, default=0)
    is_template = Column(Integer, default=0)
    status = Column(String(50), default="Open")
    priority = Column(String(20), default="Medium")
    is_important = Column(Integer, default=0)
    task_weight = Column(Float, nullable=True)
    parent_task = Column(String(255), ForeignKey("tasks.name"), nullable=True)
    completed_by = Column(String(255), nullable=True)
    completed_on = Column(DateTime(timezone=True), nullable=True)
    assigned_to = Column(String(255), nullable=True)
    exp_start_date = Column(DateTime(timezone=True), nullable=True)
    expected_time = Column(Float, nullable=True)
    start = Column(Integer, nullable=True)
    exp_end_date = Column(DateTime(timezone=True), nullable=True)
    progress = Column(Float, default=0)
    duration = Column(Integer, nullable=True)
    is_milestone = Column(Integer, default=0)
    description = Column(Text, nullable=True)
    depends_on_tasks = Column(Text, nullable=True)
    act_start_date = Column(DateTime(timezone=True), nullable=True)
    actual_time = Column(Float, nullable=True)
    act_end_date = Column(DateTime(timezone=True), nullable=True)
    total_costing_amount = Column(Float, nullable=True)
    total_expense_claim = Column(Float, nullable=True)
    total_billing_amount = Column(Float, nullable=True)
    review_date = Column(DateTime(timezone=True), nullable=True)
    closing_date = Column(DateTime(timezone=True), nullable=True)
    department = Column(String(255), nullable=True)
    company = Column(String(255), nullable=True)
    lft = Column(Integer, nullable=True)
    rgt = Column(Integer, nullable=True)
    old_parent = Column(String(255), nullable=True)
    template_task = Column(String(255), nullable=True)
    
    # Relationships
    project_rel = relationship("Project", back_populates="tasks")
    depends_on = relationship("TaskDependsOn", back_populates="task_rel", cascade="all, delete-orphan")
    parent_task_rel = relationship("Task", remote_side=[name], backref="subtasks")
