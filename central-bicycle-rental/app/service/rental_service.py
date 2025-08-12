from fastapi import HTTPException, status
from datetime import datetime
from app.repository import UserRepository
from app.model import Rental
from app.dto import RentalDTO, RentalSuccessDTO, ReturnRentalDTO, ReturnRentalSuccessDTO

class RentalService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def rent(self, rental_dto: RentalDTO):
        user = self.user_repository.get_by_national_id(rental_dto.national_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"User with national ID {rental_dto.national_id} not found."
            )

        if user.count_active_rentals() >= 2:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail="Rental limit reached: User currently has 2 active bicycle rentals."
            )

        new_rental = Rental(
            bicycle_id=rental_dto.bicycle_id,
            rental_date=rental_dto.rental_date,
            rental_end_date=None
        )

        user.add_rental(new_rental)

        user = self.user_repository.save(user)

        rental = None
        for r in user.rental_record.rentals:
            if r.bicycle_id == new_rental.bicycle_id and r.rental_date == new_rental.rental_date:
                rental = r
                break

        return RentalSuccessDTO(
            id=rental.id,
            national_id=user.national_id,
            bicycle_id=rental.bicycle_id,
            rental_date=rental.rental_date
        )
    
    def return_rental(self, return_dto: ReturnRentalDTO) -> ReturnRentalSuccessDTO:
        user = self.user_repository.get_by_national_id(return_dto.national_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with national ID {return_dto.national_id} not found."
            )
        
        rental = user.return_rental(return_dto.bicycle_id)
        if not rental:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No active rental found for bicycle ID {return_dto.bicycle_id} for user {return_dto.national_id}."
            )
        
        self.user_repository.save(user)
        
        return ReturnRentalSuccessDTO(
            id=rental.id,
            national_id=user.national_id,
            bicycle_id=rental.bicycle_id,
            rental_date=rental.rental_date,
            rental_end_date=rental.rental_end_date
        )
