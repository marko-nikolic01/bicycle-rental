from fastapi import APIRouter, status
from app.service import RegistrationService
from app.dto import RegistrationDTO

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/", response_model=None, status_code=status.HTTP_201_CREATED)
def register(registration_dto: RegistrationDTO):
    registration_service = RegistrationService()
    return registration_service.register(registration_dto)
