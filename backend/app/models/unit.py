from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base

class Unit(Base):

    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    symbol = Column(String(10), nullable=False)
    is_active = Column(Boolean, default=True)