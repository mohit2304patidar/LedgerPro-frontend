from app.models.financial_year import FinancialYear

def create_financial_year(db, data):
    fy = FinancialYear( **data.dict())
    db.add(fy)
    db.commit()
    db.refresh(fy)

    return fy

def get_all_financial_years(db):
    return (db.query(FinancialYear).all())

def get_active_financial_year(db):
    return (
        db.query(
            FinancialYear
        ).filter(
            FinancialYear.is_active == True
        ).first()
    )

def activate_financial_year(db, fy_id):
    db.query(
        FinancialYear
    ).update(
        {
            "is_active": False
        }
    )

    fy = (
        db.query(
            FinancialYear
        ).filter(
            FinancialYear.id == fy_id
        ).first()
    )

    fy.is_active = True
    db.commit()
    return fy