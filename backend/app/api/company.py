from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.company import CompanyCreate, CompanyResponse, CompanyUpdate
from app.services.company_service import (
    create_company_service,
    get_companies_service, 
    get_company_service,
    get_my_companies_service, 
    update_company_service, 
    delete_company_service
)
from app.auth.current_user import get_current_active_user

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)

@router.post("/",
             response_model=CompanyResponse
)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    #current_user = Depends(get_current_active_user)
):
    return create_company_service(
        db,
        company,
        1 #current_user.id
    )

@router.get("/",
            response_model=list[CompanyResponse]
)
def get_companies(db: Session = Depends(get_db)):
    return get_companies_service(db)

#@router.get("/my")
def my_companies(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_active_user)
):
    return get_my_companies_service(db, current_user.id)

@router.get(
    "/{company_id}",
    response_model = CompanyResponse
)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
    #current_user = Depends(
    #   get_current_active_user
    #)
):
    company = get_company_service(db, company_id)

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company Not Found"
        )
    
    #if company.owner_id != current_user.id:
    #    raise HTTPException(
    #       status_code=403,
    #       detail="Access Denied"
    #  )
    return company

@router.put(
    "/{company_id}",
    response_model = CompanyResponse
)
def update_company_route(
    company_id: int,
    update_data: CompanyUpdate,
    db: Session = Depends(get_db),
    #current_user = Depends(get_current_active_user)
):
    company = get_companies_service(db, company_id)
    
    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not Found"
        )
    
    #if company.owner_id != current_user.id:
    #   raise HTTPException(
    #       status_code=403,
    #       detail="Access Denied"
    #   )
    
    return update_company_service(
        db, company, update_data
    )

@router.delete(
    "/{company_id}"
)
def delete_company_route(
    company_id: int,
    db: Session = Depends(get_db),
    #current_user = Depends(get_current_active_user)
):
    company = get_companies_service(db, company_id)

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company Not Found"
        )
    
    #if company.owner_id != current_user.id:
    #    raise HTTPException(
    #        status_code=403,
    #        detail="Access Denied"
    #    )
    
    delete_company_service(db, company)

    return {
        "message": "Company Deleted Succesfully"
    }