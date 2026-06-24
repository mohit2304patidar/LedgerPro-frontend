from app.repositories.company_repository import create_company, get_companies, get_user_companies, get_company_by_id, update_company, delete_company
from app.repositories.user_repository import set_current_company

def create_company_service(
        db,
        company_data,
        owner_id
):
    return create_company(
        db,
        company_data,
        owner_id
    )

def get_companies_service(db):
    return get_companies(db)

def get_company_service(db, company_id):
    return get_company_by_id(db, company_id)
def get_my_companies_service(db, user_id):
    return get_user_companies(db, user_id)


def update_company_service(db, company, update_data):
    return update_company(db, company, update_data)

def select_company_service(db, user, company_id):
    return set_current_company(db, user, company_id)

def delete_company_service(db, company):
    delete_company(db, company)

