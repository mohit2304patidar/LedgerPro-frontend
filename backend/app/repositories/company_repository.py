from sqlalchemy.orm import Session
from app.models.company import Company

def create_company(
        db: Session,
        company_data,
        owner_id
):
    company = Company(
        **company_data.model_dump(),
        owner_id = owner_id
    )

    db.add(company)
    db.commit()
    db.refresh(company)

    return company

def get_companies(
        db:Session
):
    return db.query(Company).all()

def get_user_companies(db: Session, user_id):
    return db.query(Company).filter(Company.owner_id == user_id).all()

def get_company_by_id(db, company_id):
    return db.query(Company).filter(
        Company.id == company_id
    ).first()

def update_company(db, company, update_data):
    for key, value in update_data.model.dump().items():
        setattr(company, key, value)
    
    db.commit()
    db.refresh(company)

    return company

def delete_company(db, company):
    db.delete(company)
    db.commit()