from app.repositories.cutomer_repository import create_customer, get_customers

def create_customer_service(db, customer_data):
    return create_customer(db, customer_data)

def get_customers_service(db):
    return get_customers(db)