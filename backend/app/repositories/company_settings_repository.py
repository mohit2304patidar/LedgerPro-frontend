from app.models.company_settings import CompanySettings

def create_company_settings(db, data):

    existing = (
        db.query(CompanySettings)
        .first()
    )

    if existing:
        return existing
    
    company = CompanySettings(**data.dict())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

def get_company_settings(db):
    return (
        db.query(CompanySettings)
        .first()
    )

def update_company_settings(db, data):

    company = (
        db.query(
            CompanySettings
        ).first()
    )

    if not company:
        return None
    
    for key, value in data.dict().items:
        setattr(
            company,
            key,
            value
        )

    db.commit()
    db.refresh(company)

    return company