from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.purchase import PurchaseCreate
from app.services.purchase_service import create_purchase_service, get_all_purchases_service

router = APIRouter(
    prefix="/purchases",
    tags=["Purchases"]
)

@router.post("/")
def create_purchase(
    purchase: PurchaseCreate,
    db: Session = Depends(get_db)
):
    return create_purchase_service(db, purchase)

@router.get("/")
def purchase_list(db: Session = Depends(get_db)):
    return get_all_purchases_service(db)