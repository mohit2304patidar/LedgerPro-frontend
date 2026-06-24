from app.repositories.ledger_repository import create_ledger, get_ledgers, get_ledger_balance

def create_ledger_service(db, ledger_data):
    return create_ledger(db, ledger_data)

def get_ledgers_service(db):
    return get_ledgers(db)

def get_ledger_balance_service(db, ledger_id):
    return get_ledger_balance(db, ledger_id)