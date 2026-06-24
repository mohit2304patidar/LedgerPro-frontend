from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.ledger_group import LedgerGroupCreate, LedgerGroupResponse
from app.services.ledger_group_service import create_group_service, get_groups_service

router = APIRouter(
    prefix="/ledger-groups",
    tags=["Ledger Groups"]
)

@router.post(
    "/",
    response_model=LedgerGroupResponse
)
def create_group(
    group: LedgerGroupCreate,
    db: Session = Depends(get_db)
):
    return create_group_service(db, group)

@router.get(
    "/",
    response_model=list[LedgerGroupResponse]
)
def get_groups(
    db: Session = Depends(get_db)
):
    return get_groups_service(db)