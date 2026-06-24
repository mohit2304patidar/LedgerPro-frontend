from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class LedgerGroup(Base):
    __tablename__ = "ledger_groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    parent_group = Column(String(255), nullable=True)
    nature = Column(String(50), nullable=False)
    company_id = Column(Integer, nullable=True)
    is_system = Column(Boolean, default=False)
    created_at = Column(
        DateTime(timezone=True), 
        server_default = func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )