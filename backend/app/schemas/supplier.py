from pydantic import BaseModel, EmailStr

class SupplierCreate(BaseModel):
    supplier_code: str
    name: str
    mobile: str | None = None
    email: EmailStr | None = None
    gst_number: str | None = None
    pan_number: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None

class SupplierResponse(SupplierCreate):
    id: int

    class Config:
        from_attributes = True