from pydantic import BaseModel
from datetime import date

class SaleItemCreate(BaseModel):
    product_id: int
    quantity: float
    rate: float

class SaleCreate(BaseModel):
    customer_id: int
    sale_date: date
    items: list[SaleItemCreate]
    total_amount: float
    gst_rate: float = 18
    intra_state: bool = True