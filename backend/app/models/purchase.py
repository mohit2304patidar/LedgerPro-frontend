from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from app.database.database import Base

class Purchase(Base):

    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    voucher_no = Column(String, unique=True)
    purchase_date = Column(Date)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    total_amount = Column(Numeric(15,2))
    taxable_amount = Column(Numeric(15,2), default=0)
    cgst_amount = Column(Numeric(15,2), default=0)
    sgst_amount = Column(Numeric(15,2), default=0)
    igst_amount = Column(Numeric(15,2), default=0)
    total_tax = Column(Numeric(15,2), default=0)
    financial_year_id = Column(Integer, ForeignKey("financial_years.id"))