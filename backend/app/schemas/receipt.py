from datetime import date
from pydantic import BaseModel

class ReceiptCreate(BaseModel):
    receipt_date: date
    customer_id: int
    bank_ledger_id: int
    amount: float
    narration: str | None = None