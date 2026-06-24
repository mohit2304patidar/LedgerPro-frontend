from sqlalchemy import Column, Integer, Numeric, ForeignKey
from app.database.database import Base

class PurchaseItem(Base):

    __tablename__ = "purchase_items"
    id = Column(Integer, primary_key=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Numeric(15,2))
    rate = Column(Numeric(15,2))
    amount = Column(Numeric(15,2))