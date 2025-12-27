from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class ProjectUser(Base):
    __tablename__ = "project_users"
    
    name = Column(String(255), primary_key=True, index=True)
    creation = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())
    owner = Column(String(255), nullable=False)
    modified_by = Column(String(255))
    docstatus = Column(Integer, default=0)
    parent = Column(String(255), ForeignKey("projects.name"), nullable=True)
    parentfield = Column(String(255), nullable=True)
    parenttype = Column(String(255), nullable=True)
    idx = Column(Integer, nullable=True)
    
    # ProjectUser specific fields
    user = Column(String(255), nullable=True)
    role = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    view_attachments = Column(Integer, default=1)
    welcome_email_sent = Column(Integer, default=0)
    
    # Relationships
    project = relationship("Project", back_populates="users")
