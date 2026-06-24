from app.repositories.stock_repository import create_stock_movement, get_stock_summary, get_stock_ledger

def create_stock_movement_service(db, stock_data):
    return create_stock_movement(db, stock_data)

def get_stock_summary_service(db):
    return get_stock_summary(db)

def get_stock_ledger_service(db, product_id: int):
    return get_stock_ledger(db, product_id)