from app.repositories.unit_repository import *

def create_unit_service(db, unit_data):
    return create_unit(db, unit_data)

def get_units_service(db):
    return get_units(db)