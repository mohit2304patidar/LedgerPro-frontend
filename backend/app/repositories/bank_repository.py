from app.models.bank_account import BankAccount

def create_bank_account(db, bank_data):
    bank = BankAccount(
        **bank_data.model_dump()
    )
    db.add(bank)
    db.commit()
    db.refresh(bank)
    return bank

def get_all_bank_accounts(db):
    return (db.query(BankAccount).all())