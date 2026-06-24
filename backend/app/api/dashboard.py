from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.dashboard_service import (
    get_dashboard_Service, 
    get_top_selling_products_service,
    get_low_stock_products_service,
    get_monthly_sales_service,
    get_monthly_purchase_service
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/")
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard_Service(db)

@router.get("/top-products")
def top_products(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_top_selling_products_service(db, limit)

@router.get("/low-stock")
def low_stock_products(
    threshold: int = 5,
    db: Session = Depends(get_db)
):
    return get_low_stock_products_service(db, threshold)

@router.get("/monthly-sales")
def monthly_sales(db: Session = Depends(get_db)):
    return get_monthly_sales_service(db)

@router.get("/monthly-purchase")
def monthly_purchase(db: Session = Depends(get_db)):
    return get_monthly_purchase_service(db)