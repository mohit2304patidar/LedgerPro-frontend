from app.repositories.bank_repository import create_bank_account, get_all_bank_accounts

def create_bank_account_service(db, bank_data):
    return create_bank_account(db, bank_data)

def get_all_bank_accounts_service(db):
    return get_all_bank_accounts(db)