from app.repositories.product_repository import create_product
from app.models.product import Product

def create_product_service(db, product_data):
    return create_product(db, product_data)

def get_products_service(db):
    return db.query(Product).all()