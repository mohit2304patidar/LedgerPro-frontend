from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class StockMovement(Base):

    __tablename__ = "stock_movements"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    movement_type = Column(String, nullable=False)
    quantity = Column(Numeric(15, 2), nullable=False)
    rate = Column(Numeric(15,2), nullable=True)
    reference_type = Column(String)
    reference_id = Column(Integer)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )