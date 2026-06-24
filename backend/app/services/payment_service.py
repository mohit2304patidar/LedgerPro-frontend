from app.repositories.payment_repository import create_payment

def create_payment_service(db, payment_data):
    return create_payment(db, payment_data)