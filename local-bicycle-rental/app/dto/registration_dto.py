from pydantic import BaseModel, constr
from .registration_address_dto import RegistrationAddressDTO

class RegistrationDTO(BaseModel):
    name: str
    last_name: str
    national_id: constr(min_length=13, max_length=13)
    address: RegistrationAddressDTO
