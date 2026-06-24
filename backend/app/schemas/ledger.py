from pydantic import BaseModel
from typing import Optional

class LedgerCreate(BaseModel):
    name: str
    group_id: Optional[int] = None
    ledger_type: str = "GENERAL"
    opening_balance: Optional[float] = 0
    balance_type: Optional[str] = "Dr"
    gst_numbers: str | None = None
    pan_numbers: str | None = None
    mobiles: str | None = None
    email: str | None = None
    address: str | None = None


class LedgerResponse(LedgerCreate):
    id: int

    class Config:
        from_attributes = True