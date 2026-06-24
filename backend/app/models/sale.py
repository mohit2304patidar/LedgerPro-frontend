from sqlalchemy import Column, Integer,String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Sale(Base):

    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    voucher_no = Column(String, unique=True, nullable=False)
    sale_date = Column(Date)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    sale_items = relationship("SaleItem", back_populates="sale", cascade="all, delete-orphan")
    total_amount = Column(Numeric(15,2), default=0)
    taxable_amount = Column(Numeric(15,2), default=0)
    cgst_amount = Column(Numeric(15,2), default=0)
    sgst_amount = Column(Numeric(15,2), default=0)
    igst_amount = Column(Numeric(15,2), default=0)
    total_tax = Column(Numeric(15,2), default=0)
    financial_year_id = Column(Integer, ForeignKey("financial_years.id"))