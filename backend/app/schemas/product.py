from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    sku: str
    category_id: int
    unit_id: int
    hsn_code: str
    gst_rate: float
    purchase_rate: float
    sale_rate: float
    opening_stock: float


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True