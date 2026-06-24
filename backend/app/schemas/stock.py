from pydantic import BaseModel

class StockMovementCreate(BaseModel):
    product_id: int
    movement_type: str
    quantity: float
    rate: float | None = None
    reference_type: str | None = None
    reference_id : int | None = None