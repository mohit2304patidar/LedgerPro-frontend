from sqlalchemy import *
from sqlalchemy.sql import func
from app.database.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key= True)
    supplier_code = Column(String(50), unique=True)
    name = Column(String(255)) 
    mobile = Column(String(20)) 
    email = Column(String(255)) 
    gst_number = Column(String(50)) 
    pan_number = Column(String(20)) 
    address = Column(String(500)) 
    city = Column(String(200)) 
    state = Column(String(100)) 
    ledger_id = Column(Integer) 
    company_id = Column(Integer) 
    is_active = Column(Boolean, default=True) 
    created_at = Column(DateTime(timezone=true),
                        server_default=func.now()
                    ) 
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )