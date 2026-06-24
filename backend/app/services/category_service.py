from app.repositories.category_repository import create_category, get_categories

def create_category_service(db, category_data):
    return create_category(db, category_data)

def get_categories_service(db):
    return get_categories(db)