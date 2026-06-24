from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User

def get_current_active_user(
        payload = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == payload["user_id"]
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    
    return user