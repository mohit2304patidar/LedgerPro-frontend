from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import create_product_service, get_products_service


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return create_product_service(db, product)

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return get_products_service(db)