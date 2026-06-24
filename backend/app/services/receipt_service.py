from app.repositories.receipt_repository import create_receipt

def create_receipt_service(db, receipt_data):
    return create_receipt(db, receipt_data)