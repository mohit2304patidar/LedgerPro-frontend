from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.transaction import TransactionCreate
from app.services.transaction_service import (
    create_transaction_service, 
    get_transactions_service,
    get_daybook_service,
    get_ledger_statement_service,
    get_trial_balance_service,
    get_profit_loss_service,
    get_balance_sheet_service,
    get_cash_flow_service
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("/")
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return create_transaction_service(db, transaction)

@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return get_transactions_service(db)

@router.get("/daybook")
def daybook(db: Session = Depends(get_db)):
    return get_daybook_service(db)

@router.get("/ledger-statement/{ledger_id}")
def ledger_statement(
    ledger_id: int,
    db: Session = Depends(get_db)
):
    return get_ledger_statement_service(db, ledger_id)

@router.get("/trial-balance")
def trial_balance(db: Session = Depends(get_db)):
    return get_trial_balance_service(db)

@router.get("/profit-loss")
def profit_loss(db: Session = Depends(get_db)):
    return get_profit_loss_service(db)

@router.get("/balance-sheet")
def balance_sheet(db: Session = Depends(get_db)):
    return get_balance_sheet_service(db)

@router.get("/cash-flow")
def cash_flow(db: Session = Depends(get_db)):
    return get_cash_flow_service(db)