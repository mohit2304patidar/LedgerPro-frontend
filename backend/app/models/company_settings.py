from sqlalchemy import Column, Integer, String
from app.database.database import Base

class CompanySettings(Base):

    __tablename__ = "company_settings"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(200), nullable=False)
    gst_number = Column(String(30), nullable=True)
    pan_number = Column(String(20), nullable=True)
    mobile = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    address = Column(String(500), nullable=True)
    financial_year = Column(String(20), nullable=False)
    logo_url = Column(String(500), nullable=True)