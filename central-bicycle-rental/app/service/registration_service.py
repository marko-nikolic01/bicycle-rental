from fastapi import HTTPException, status
from app.repository import UserRepository
from app.model import User, Address
from app.dto import RegistrationDTO, RegistrationSuccessDTO, RegistrationSuccessAddressDTO

class RegistrationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, registration_dto: RegistrationDTO) -> RegistrationSuccessDTO:
        existing_user = self.user_repository.get_by_national_id(registration_dto.national_id)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User with national ID {registration_dto.national_id} already exists."
            )

        address = Address(
            country=registration_dto.address.country,
            city=registration_dto.address.city,
            street=registration_dto.address.street,
            number=registration_dto.address.number
        )

        user = User(
            name=registration_dto.name,
            last_name=registration_dto.last_name,
            national_id=registration_dto.national_id,
            address=address
        )

        saved_user = self.user_repository.save(user)

        return RegistrationSuccessDTO(
            id=saved_user.id,
            name=saved_user.name,
            last_name=saved_user.last_name,
            national_id=saved_user.national_id,
            address=RegistrationSuccessAddressDTO(
                country=saved_user.address.country,
                city=saved_user.address.city,
                street=saved_user.address.street,
                number=saved_user.address.number
            )
        )
