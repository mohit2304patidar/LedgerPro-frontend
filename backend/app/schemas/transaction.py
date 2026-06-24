from pydantic import BaseModel
from typing import List

class EntryCreate(BaseModel):
    ledger_id: int
    debit: float = 0
    credit: float = 0

class TransactionCreate(BaseModel):

    voucher_type: str
    narrations: str
    entries: List[EntryCreate]
    