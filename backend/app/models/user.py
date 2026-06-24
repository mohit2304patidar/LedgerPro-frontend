from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    current_company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)
    companies = relationship("Company", back_populates="owner",foreign_keys="Company.owner_id")
    current_company = relationship("Company", foreign_keys=[current_company_id])
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default = func.now(),
        onupdate = func.now()
    )