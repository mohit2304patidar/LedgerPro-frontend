from app.repositories.supplier_repository import create_supplier, get_suppliers

def create_supplier_service(db, supplier_data):
    return create_supplier(db, supplier_data)

def get_suppliers_service(db):
    return get_suppliers(db)