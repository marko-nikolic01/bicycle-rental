from pydantic import BaseModel
from uuid import UUID
from .registration_success_address_dto import RegistrationSuccessAddressDTO

class RegistrationSuccessDTO(BaseModel):
    id: UUID
    name: str
    last_name: str
    national_id: str
    address: RegistrationSuccessAddressDTO

    class Config:
        orm_mode = True
