from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.bank_account import BankAccountCreate
from app.services.bank_service import (
    create_bank_account_service,
    get_all_bank_accounts_service
)

router = APIRouter(
    prefix="/banks",
    tags=["Banks"]
)

@router.post("/")
def create_bank(
    bank: BankAccountCreate,
    db: Session = Depends(get_db)
):
    return create_bank_account_service(db, bank)

@router.get("/")
def get_banks(db: Session = Depends(get_db)):
    return get_all_bank_accounts_service(db)