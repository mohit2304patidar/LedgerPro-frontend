from pydantic import BaseModel, EmailStr

class CompanyCreate(BaseModel):
    company_name: str
    owner_name: str
    email: EmailStr
    phone: str
    address: str
    state: str
    country: str = "India"
    financial_year: str

class CompanyUpdate(BaseModel):
    company_name: str
    owner_name: str
    email: EmailStr
    phone: str
    address: str
    state: str
    country: str
    financial_year: str


class CompanyResponse(BaseModel):
    id: int
    company_name: str
    owner_name: str
    email: EmailStr
    phone: str
    address: str
    state: str
    country: str
    financial_year: str

    class Config:
        from_attributes = True