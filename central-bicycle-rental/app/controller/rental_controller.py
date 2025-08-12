from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.repository import UserRepository
from app.service import RentalService
from app.dto import RentalDTO, RentalSuccessDTO, ReturnRentalDTO, ReturnRentalSuccessDTO

router = APIRouter(prefix="/api/rentals", tags=["Rentals"])

@router.post("/", response_model=RentalSuccessDTO, status_code=status.HTTP_201_CREATED)
def rent(rental_dto: RentalDTO, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    rental_service = RentalService(user_repository)

    return rental_service.rent(rental_dto)

@router.delete("/", response_model=ReturnRentalSuccessDTO, status_code=status.HTTP_200_OK)
def return_rental(return_dto: ReturnRentalDTO, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    rental_service = RentalService(user_repository)

    return rental_service.return_rental(return_dto)
