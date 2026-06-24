from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.stock import StockMovementCreate
from app.services.stock_service import (
    create_stock_movement_service, 
    get_stock_summary_service, 
    get_stock_ledger_service
)

router = APIRouter(
    prefix="/stock",
    tags=["stock"]
)

@router.post("/")
def create_stock(
    stock: StockMovementCreate,
    db: Session = Depends(get_db)
):
    return create_stock_movement_service(db, stock)

@router.get("/summary")
def stock_summary(db: Session = Depends(get_db)):
    return get_stock_summary_service(db)

@router.get("/ledger/{product_id}")
def stock_ledger(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_stock_ledger_service(db, product_id)