from fastapi import HTTPException
from app.repositories.transaction_repository import (
    create_transaction, 
    get_transactions, 
    get_daybook, 
    get_ledger_statement,
    get_trial_balance,
    get_profit_loss,
    get_balance_sheet,
    get_cash_flow
)

def create_transaction_service(db, transaction_data):
    total_debit = sum(
        entry.debit
        for entry in transaction_data.entries
    )

    total_credit = sum(
        entry.credit
        for entry in transaction_data.entries
    )

    if total_debit != total_credit:

        raise HTTPException(
            status_code=400,
            detail="Voucher not balanced"
        )
    
    return create_transaction(db, transaction_data)

def get_transactions_service(db):
    return get_transactions(db)

def get_daybook_service(db):
    return get_daybook(db)

def get_ledger_statement_service(db, ledger_id):
    return get_ledger_statement(db, ledger_id)

def get_trial_balance_service(db):
    return get_trial_balance(db)

def get_profit_loss_service(db):
    return get_profit_loss(db)

def get_balance_sheet_service(db):
    return get_balance_sheet(db)

def get_cash_flow_service(db):
    return get_cash_flow(db)