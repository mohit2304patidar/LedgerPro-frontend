from sqlalchemy import func
from app.models.ledger import Ledger
from app.models.transaction_entry import TransactionEntry

def create_ledger(db, ledger_data):
    print(ledger_data.model_dump())
    ledger = Ledger(
        **ledger_data.model_dump()
    )
    db.add(ledger)
    db.commit()
    db.refresh(ledger)
    return ledger

def get_ledgers(db):
    return db.query(Ledger).all()

def get_ledger_by_id(db, ledger_id):
    return (
        db.query(Ledger)
        .filter(Ledger.id == ledger_id)
        .first()
    ) 

def get_ledger_balance(db, ledger_id):
    ledger = get_ledger_by_id(db, ledger_id)
    total_debit = (
        db.query(
            func.coalesce(
                func.sum(TransactionEntry.debit),
                0
            )
        )
        .filter(
            TransactionEntry.ledger_id == ledger_id
        )
        .scalar()
    )

    total_credit = (
        db.query(
            func.coalesce(
                func.sum(TransactionEntry.credit),
                0
            )
        )
        .filter(
            TransactionEntry.ledger_id == ledger_id
        )
        .scalar()
    )

    balance = (
        ledger.opening_balance
        + total_debit
        - total_credit
    )

    return {
        "ledger_id": ledger.id,
        "ledger_name": ledger.name,
        "opening_balance": float(
            ledger.opening_balance
        ),
        "total_debt": float (
            total_debit
        ),
        "total_credit": float (
            total_credit
        ),
        "current_balance": float(
            balance
        )
    }

def get_system_ledger(db, system_code):
    ledger = (
        db.query(Ledger)
        .filter(
            Ledger.system_code == system_code
        )
        .first()
    )

    if not ledger:
        raise Exception(
            f"System Ledger {system_code} not found"
        )
    return ledger