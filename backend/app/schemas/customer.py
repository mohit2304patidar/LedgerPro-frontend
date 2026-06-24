from pydantic import BaseModel, EmailStr

class CustomerCreate(BaseModel):
    customer_code: str
    name: str
    mobile: str | None = None
    email: EmailStr | None = None
    mobile: str | None = None
    gst_number: str | None = None
    pan_number: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    credit_limit: float = 0

class CustomerResponse(CustomerCreate):
    id: int
    class Config:
        from_attributes = True
        