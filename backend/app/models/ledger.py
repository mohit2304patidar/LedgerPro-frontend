from sqlalchemy import Column, Integer, String, Numeric, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.database import Base

class Ledger(Base):
    __tablename__ = "ledgers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    ledger_type = Column(String(50), default="GENERAL")
    group_id = Column(Integer, ForeignKey("ledger_groups.id"))
    system_code = Column(String(50), nullable=True, unique=True)
    opening_balance = Column(Numeric(18, 2), default=0)
    balance_type = Column(String(10), default="Dr")
    gst_number = Column(String(50), nullable=True)
    pan_number = Column(String(20), nullable=True)
    mobile = Column(String(20), nullable=True)
    email = Column(String(255), nullable=True)
    address = Column(String(500), nullable=True)
    company_id = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(
        DateTime(timezone=True), 
        server_default = func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )