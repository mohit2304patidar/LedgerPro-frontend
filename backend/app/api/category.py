from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.services.category_service import create_category_service, get_categories_service

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return create_category_service(db, category)

@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return get_categories_service(db)