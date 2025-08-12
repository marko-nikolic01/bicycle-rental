from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
import requests
import os
from app.repository import BicycleRepository
from app.model import Rental
from app.dto import RentalDTO, RentalSuccessDTO

class RentalService:
    def __init__(self, bicycle_repository: BicycleRepository):
        self.bicycle_repository = bicycle_repository

        CENTRAL_BICYCLE_RENTAL_HOST = os.getenv("CENTRAL_BICYCLE_RENTAL_HOST", "central-bicycle-rental")
        CENTRAL_BICYCLE_RENTAL_PORT = os.getenv("CENTRAL_BICYCLE_RENTAL_PORT", 8000)
        self.CENTRAL_BICYCLE_RENTAL_URL = f"http://{CENTRAL_BICYCLE_RENTAL_HOST}:{CENTRAL_BICYCLE_RENTAL_PORT}/api"

    def rent(self, rental_dto: RentalDTO):
        bicycle = self.bicycle_repository.get_by_id_and_type(rental_dto.bicycle_id, rental_dto.bicycle_type)
        if not bicycle:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Bicycle with ID {rental_dto.national_id} and type {rental_dto.bicycle_type.value} not found."
            )
        
        if not bicycle.can_rent():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=f"Bicycle with ID {rental_dto.national_id} and type {rental_dto.bicycle_type.value} is already rented."
            )

        response = requests.post(
            f"{self.CENTRAL_BICYCLE_RENTAL_URL}/rentals",
            data=rental_dto.model_dump_json(),
            headers={"Content-Type": "application/json"}
        )

        if not response.ok:
            return JSONResponse(
                status_code=response.status_code,
                content=response.json()
            )
        
        new_rental = Rental(
            user_id=rental_dto.national_id,
            rental_date=rental_dto.rental_date,
            rental_record=bicycle.rental_record
        )

        bicycle.add_rental(new_rental)

        bicycle = self.bicycle_repository.save(bicycle)

        rental = None
        for r in bicycle.rental_record.rentals:
            if r.user_id == new_rental.user_id and r.rental_date == new_rental.rental_date:
                rental = r
                break

        return RentalSuccessDTO(
            id=rental.id,
            national_id=rental.user_id,
            bicycle_id=bicycle.id,
            bicycle_type=bicycle.type,
            rental_date=rental.rental_date
        )
