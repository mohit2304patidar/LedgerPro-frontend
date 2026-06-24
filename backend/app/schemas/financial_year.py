from datetime import date
from pydantic import BaseModel

class FinancialYearCreate(BaseModel):
    fy_name: str
    start_date: date
    end_date: date


class FinancialYearResponse(FinancialYearCreate):
    id: int

    class Config:
        from_attributes = True