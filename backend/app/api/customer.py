from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.services.customer_service import create_customer_service, get_customers_service

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post(
    "/", 
    response_model=CustomerResponse 
)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_customer_service(db, customer)

@router.get(
    "/",
    response_model=list[CustomerResponse]
)
def get_customers(
    db: Session = Depends(get_db)
):
    return get_customers_service(db)