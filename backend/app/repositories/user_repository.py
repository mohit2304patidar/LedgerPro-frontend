from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(
        db: Session,
        full_name: str,
        email: str,
        password_hash: str
):
    user = User(
        full_name = full_name,
        email = email,
        password_hash = password_hash
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def set_current_company(db, user, company_id):
    user.current_company_id = company_id
    db.commit()
    db.refresh(user)
    return user