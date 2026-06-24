from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.sale import SaleCreate
from app.services.sale_service import create_sale_service, get_all_sales_service

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)

@router.post("/")
def create_sale(
    sale: SaleCreate,
    db: Session = Depends(get_db)
):
    return create_sale_service(db, sale)

@router.get("/")
def sales_list(db: Session = Depends(get_db)):
    return get_all_sales_service(db)