from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, Date
from sqlalchemy.sql import func
from app.database.database import Base

class Transaction(Base):
    
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    voucher_no = Column(String, unique=True, nullable=True)
    voucher_type = Column(String)
    transaction_date = Column(Date, nullable=False)
    amount = Column(Numeric(15,2), default=0)
    narrations = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, server_default=func.now())