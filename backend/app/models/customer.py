from sqlalchemy import *
from sqlalchemy.sql import func
from app.database.database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    customer_code = Column(String(50), unique=True)
    name = Column(String(255))
    mobile = Column(String(255))
    email = Column(String(255))
    gst_number = Column(String(255))
    pan_number = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    credit_limit = Column(Numeric(18, 2), default=0)
    ledger_id = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())