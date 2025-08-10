from pydantic import BaseModel

class RegistrationAddressDTO(BaseModel):
    country: str
    city: str
    street: str
    number: str
