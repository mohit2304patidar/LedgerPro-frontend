from app.repositories.financial_year_repository import (
    create_financial_year,
    get_all_financial_years,
    get_active_financial_year, 
    activate_financial_year
)

def create_financial_year_service(db, data):
    return create_financial_year(db, data)

def get_all_financial_years_service(db):
    return get_all_financial_years(db)

def get_active_financial_year_service(db):
    return get_active_financial_year(db)

def activate_financial_year_service(db, fy_id):
    return activate_financial_year(db, fy_id)