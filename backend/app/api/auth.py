from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin
)
from app.services.auth_services import (
    register_user,
    authenticate_user
)
from app.auth.jwt_handler import (
    create_access_token
)
from app.auth.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    created_user = register_user(
        db,
        user
    )

    if not created_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    return created_user

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    authenticated_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not authenticated_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    
    token = create_access_token(
        {
            "sub": authenticated_user.email,
            "user_id": authenticated_user.id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def me(
    current_user = Depends(
        get_current_user
    )
):
    return current_user