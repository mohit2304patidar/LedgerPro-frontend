from sqlalchemy import Column, Integer, Numeric, ForeignKey
from app.database.database import Base

class TransactionEntry(Base):

    __tablename__ = "transaction_entries"
    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    ledger_id = Column(Integer, ForeignKey("ledgers.id"))
    debit = Column(Numeric(15, 2), default=0)
    credit = Column(Numeric(15, 2), default=0)
    