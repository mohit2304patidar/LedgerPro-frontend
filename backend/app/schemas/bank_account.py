from pydantic import BaseModel

class BankAccountCreate(BaseModel):
    bank_name: str
    account_name: str
    account_number: str
    ifsc_code: str
    ledger_id: int