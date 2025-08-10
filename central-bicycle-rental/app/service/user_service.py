from fastapi import HTTPException, status
from typing import List
from app.repository import UserRepository
from app.dto import UserDetailsDTO, UserDetailsAddressDTO

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_details(self, national_id: str) -> UserDetailsDTO:
        user = self.user_repository.get_by_national_id(national_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with national ID {national_id} not found."
            )
        
        return UserDetailsDTO(
            id=user.id,
            name=user.name,
            last_name=user.last_name,
            national_id=user.national_id,
            address=UserDetailsAddressDTO(
                country=user.address.country,
                city=user.address.city,
                street=user.address.street,
                number=user.address.number
            ),
            active_rentals_count=user.count_active_rentals()
        )
    
    def get_all_user_details(self) -> List[UserDetailsDTO]:
        user_details = []

        users = self.user_repository.get_all()
        for user in users:
            user_details.append(
                UserDetailsDTO(
                    id=user.id,
                    name=user.name,
                    last_name=user.last_name,
                    national_id=user.national_id,
                    address=UserDetailsAddressDTO(
                        country=user.address.country,
                        city=user.address.city,
                        street=user.address.street,
                        number=user.address.number
                    ),
                    active_rentals_count=user.count_active_rentals()
                )
            )

        return user_details
