from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.payment import PaymentCreate
from app.services.payment_service import create_payment_service

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("/")
def create_payment_api(
    payment: PaymentCreate,
    db: Session = Depends(get_db)
):
    return create_payment_service(db, payment)