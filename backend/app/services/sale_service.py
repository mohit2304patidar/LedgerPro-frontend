from app.repositories.sale_repository import create_sale, get_all_sales

def create_sale_service(db, sale_data):
    return create_sale(db, sale_data)

def get_all_sales_service(db):
    return get_all_sales(db)