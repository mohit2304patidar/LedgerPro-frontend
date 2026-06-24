from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.company_settings import CompanySettingsCreate
from app.services.company_settings_service import (
    create_company_settings_service,
    get_company_settings_Service,
    update_company_settings_service
)

router = APIRouter(
    prefix="/company-settings",
    tags=["Company Settings"]
)

@router.post("/")
def create_company_settings(
    data: CompanySettingsCreate,
    db: Session = Depends(get_db)
):
    return create_company_settings_service(db, data)

@router.get("/")
def get_company_settings(db: Session = Depends(get_db)):
    return get_company_settings_Service(db)
@router.put("/")
def update_company_settings(
    data: CompanySettingsCreate,
    db: Session = Depends(get_db)
):
    return update_company_settings_service(db, data)