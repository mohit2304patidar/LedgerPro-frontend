from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.unit import UnitCreate
from app.services.unit_service import *

router = APIRouter(
    prefix="/units",
    tags=["units"]
)

@router.post("/")
def create_unit(
    unit: UnitCreate,
    db: Session = Depends(get_db)
):
    return create_unit_service(db, unit)

@router.get("/")
def get_all_units(db: Session = Depends(get_db)):
    return get_units_service(db)