from pydantic import BaseModel

class CompanySettingsCreate(BaseModel):
    company_name: str
    gst_number: str | None = None
    pan_number: str | None = None
    mobile: str | None = None
    email: str | None = None
    address: str | None = None
    financial_year: str
    logo_url: str | None = None

class CompanySettingsResponse(CompanySettingsCreate):
    id: int

    class Config:
        from_attributes = True