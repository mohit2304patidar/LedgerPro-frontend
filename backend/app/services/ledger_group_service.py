from app.repositories.ledger_group_repository import create_group, get_groups

def create_group_service(db, group_data):
    return create_group(db, group_data)

def get_groups_service(db):
    return get_groups(db)