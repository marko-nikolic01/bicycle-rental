from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.repository import UserRepository
from app.service import RegistrationService
from app.dto import RegistrationDTO, RegistrationSuccessDTO

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/", response_model=RegistrationSuccessDTO, status_code=status.HTTP_201_CREATED)
def register(registration_dto: RegistrationDTO, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    registration_service = RegistrationService(user_repository)
    return registration_service.register(registration_dto)
