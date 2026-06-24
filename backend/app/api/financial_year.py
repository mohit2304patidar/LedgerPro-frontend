from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.financial_year import FinancialYearCreate
from app.services.financial_year_service import (
    create_financial_year_service,
    get_active_financial_year_service,
    get_all_financial_years_service,
    activate_financial_year_service
)

router = APIRouter(
    prefix="/financial-year",
    tags=["Financial Years"]
)

@router.post("/")
def create_fy(
    data: FinancialYearCreate,
    db: Session = Depends(get_db)
):
    return create_financial_year_service(db, data)

@router.get("/")
def list_fy(db: Session = Depends(get_db)):
    return get_all_financial_years_service(db)

@router.get("/active")
def active_fy(db: Session = Depends(get_db)):
    return get_active_financial_year_service(db)

@router.put("/activate/{fy_id}")
def activate_fy(
    fy_id: int,
    db: Session = Depends(get_db)
):
    return activate_financial_year_service(db, fy_id)