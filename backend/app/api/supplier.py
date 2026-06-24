from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.supplier import SupplierCreate, SupplierResponse
from app.services.supplier_service import create_supplier_service, get_suppliers_service

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)

@router.post(
    "/",
    response_model=SupplierResponse
)
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    return create_supplier_service(db, supplier)

@router.get(
    "/",
    response_model=list[SupplierResponse]
)
def get_suppliers(
    db: Session = Depends(get_db)
):
    return get_suppliers_service(db)