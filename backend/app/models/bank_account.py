from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class BankAccount(Base):

    __tablename__ = "bank_accounts"
    id = Column(Integer, primary_key=True)
    bank_name = Column(String(255))
    account_name = Column(String(255))
    account_number = Column(String(100))
    ifsc_code = Column(String(50))
    ledger_id = Column(Integer, ForeignKey("ledgers.id"))

