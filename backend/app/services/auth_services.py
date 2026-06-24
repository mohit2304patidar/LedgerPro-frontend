from sqlalchemy.orm import Session
from app.auth.hashing import hash_password, verify_password
from app.repositories.user_repository import (
    create_user,
    get_user_by_email
)

def register_user(db: Session, user_data):
    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        return None
    
    hashed = hash_password(user_data.password)
    return create_user(
        db,
        user_data.full_name,
        user_data.email,
        hashed
    )

def authenticate_user(
        db,
        email: str,
        password: str
):
    user = get_user_by_email(
        db,
        email
    )

    if not user:
        return None
    
    if not verify_password(
        password,
        user.password_hash
    ):
        return None
    return user