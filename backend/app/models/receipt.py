from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from app.database.database import Base

class Receipt(Base):

    __tablename__ = "receipts"
    id = Column(Integer, primary_key=True)
    voucher_no = Column(String, unique=True)
    receipt_date = Column(Date)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    bank_ledger_id = Column(Integer, ForeignKey("ledgers.id"))
    financial_year_id = Column(Integer, ForeignKey("financial_years.id"))
    amount = Column(Numeric(15,2))
    narration = Column(String)