from sqlalchemy import Column, Integer, String, Date, Boolean
from app.database.database import Base

class FinancialYear(Base):

    __tablename__ = "financial_years"
    id = Column(Integer, primary_key=True, index=True)
    fy_name = Column(String(20), unique=True, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=False)
    