from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.receipt import ReceiptCreate
from app.services.receipt_service import create_receipt_service

router = APIRouter(
    prefix="/receipts",
    tags=["Receipts"]
)

@router.post("/")
def create_receipt_api(
    receipt: ReceiptCreate,
    db: Session = Depends(get_db)
):
    return create_receipt_service(db, receipt)