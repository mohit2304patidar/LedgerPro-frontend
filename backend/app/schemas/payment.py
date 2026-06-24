from datetime import date
from pydantic import BaseModel

class PaymentCreate(BaseModel):
    payment_date: date
    supplier_id: int
    bank_ledger_id: int
    amount: float
    narration: str | None = None