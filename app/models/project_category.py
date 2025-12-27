from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class ProjectCategory(Base):
    __tablename__ = "project_categories"
    
    name = Column(String(255), primary_key=True, index=True)
    creation = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())
    owner = Column(String(255), nullable=False)
    modified_by = Column(String(255))
    docstatus = Column(Integer, default=0)
    
    # ProjectCategory specific fields
    category_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    # Relationships
    projects = relationship("Project", back_populates="category_details")
