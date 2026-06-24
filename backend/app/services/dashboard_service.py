from app.repositories.dashboard_repository import (
    get_dashboard_data,
    get_top_selling_products,
    get_low_stock_products,
    get_monthly_sales,
    get_monthly_purchase
)

def get_dashboard_Service(db):
    return get_dashboard_data(db)

def get_top_selling_products_service(db, limit=10):
    return get_top_selling_products(db, limit)

def get_low_stock_products_service(db, threshold = 5):
    return get_low_stock_products(db, threshold)

def get_monthly_sales_service(db):
    return get_monthly_sales(db)

def get_monthly_purchase_service(db):
    return get_monthly_purchase(db)