from pydantic import BaseModel
from datetime import date

class PurchaseItemCreate(BaseModel):
    product_id: int
    quantity: float
    rate: float

class PurchaseCreate(BaseModel):
    supplier_id: int
    purchase_date: date
    items: list[PurchaseItemCreate]
    supplier_id: int
    total_amount: float
    gst_rate: float = 18
    intra_state: bool = True