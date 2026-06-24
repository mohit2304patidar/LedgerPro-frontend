from app.repositories.purchase_repository import create_purchase, get_all_purchases

def create_purchase_service(db, purchase_data):
    return create_purchase(db, purchase_data)

def get_all_purchases_service(db):
    return get_all_purchases(db)