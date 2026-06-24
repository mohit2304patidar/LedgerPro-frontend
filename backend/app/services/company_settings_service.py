from app.repositories.company_settings_repository import (
    create_company_settings,
    get_company_settings,
    update_company_settings
)

def create_company_settings_service(db, data):
    return create_company_settings(db, data)

def get_company_settings_Service(db):
    return get_company_settings(db)

def update_company_settings_service(db, data):
    return update_company_settings(db, data)