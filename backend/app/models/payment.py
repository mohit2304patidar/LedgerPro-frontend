from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from app.database.database import Base

class Payment(Base):

    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    voucher_no = Column(String, unique=True, nullable=False)
    payment_date = Column(Date, nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    bank_ledger_id = Column(Integer, ForeignKey("ledgers.id"), nullable=False)
    financial_year_id = Column(Integer, ForeignKey("financial_years.id"), nullable=False)
    amount = Column(Numeric(15,2), nullable=False)
    narration = Column(String)
    