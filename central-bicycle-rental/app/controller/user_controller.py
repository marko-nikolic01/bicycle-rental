from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.repository import UserRepository
from app.service import UserService
from app.dto import UserDetailsDTO

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{national_id}", response_model=UserDetailsDTO, status_code=status.HTTP_200_OK)
def get_user_details(national_id: str, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)

    return user_service.get_user_details(national_id)
