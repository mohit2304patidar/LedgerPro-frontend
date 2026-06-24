from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class SaleItem(Base):
    
    __tablename__ = "sale_items"
    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    sale = relationship("Sale", back_populates="sale_items")
    quantity = Column(Numeric(15,2))
    rate = Column(Numeric(15,2))
    amount = Column(Numeric(15,2))