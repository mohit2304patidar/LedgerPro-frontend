from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from app.database.database import Base

class Product(Base):

    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    sku = Column(String(100), unique=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    unit_id = Column(Integer, ForeignKey("units.id"))
    hsn_code = Column(String(50))
    gst_rate = Column(Numeric(5,2), default=18)
    purchase_rate = Column(Numeric(15,2), default=0)
    sale_rate = Column(Numeric(15,2), default=0)
    opening_stock = Column(Numeric(15,2), default=0)
    is_active = Column(Boolean, default=True)