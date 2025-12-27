from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class TaskDependsOn(Base):
    __tablename__ = "task_depends_on"
    
    name = Column(String(255), primary_key=True, index=True)
    creation = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())
    owner = Column(String(255), nullable=False)
    modified_by = Column(String(255))
    docstatus = Column(Integer, default=0)  # 0, 1, 2
    parent = Column(String(255), ForeignKey("tasks.name"), nullable=True)
    parentfield = Column(String(255), nullable=True)
    parenttype = Column(String(255), nullable=True)
    idx = Column(Integer, nullable=True)
    
    # TaskDependsOn specific fields
    task = Column(String(255), nullable=True)
    subject = Column(Text, nullable=True)
    project = Column(Text, nullable=True)
    
    # Relationships
    task_rel = relationship("Task", back_populates="depends_on")
