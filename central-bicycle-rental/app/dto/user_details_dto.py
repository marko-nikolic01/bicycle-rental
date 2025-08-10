from pydantic import BaseModel
from uuid import UUID
from .user_details_address_dto import UserDetailsAddressDTO

class UserDetailsDTO(BaseModel):
    id: UUID
    name: str
    last_name: str
    national_id: str
    address: UserDetailsAddressDTO 
    active_rentals_count: int
