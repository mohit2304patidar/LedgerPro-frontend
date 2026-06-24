from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.ledger import LedgerCreate, LedgerResponse
from app.services.ledger_service import create_ledger_service, get_ledgers_service, get_ledger_balance_service

router = APIRouter(
    prefix="/ledgers",
    tags=["Ledgers"]
)

@router.post(
    "/",
    response_model=LedgerResponse
)
def create_ledger(
    ledger: LedgerCreate,
    db: Session = Depends(get_db)
):
    return create_ledger_service(db, ledger)

@router.get(
    "/",
    response_model=list[LedgerResponse]
)
def get_ledgers(db: Session = Depends(get_db)):
    return get_ledgers_service(db)

@router.get("/{ledger_id}/balance")
def ledger_balance(
    ledger_id: int,
    db: Session = Depends(get_db)
):
    return get_ledger_balance_service(db, ledger_id)