from pydantic import BaseModel

class RegistrationSuccessAddressDTO(BaseModel):
    country: str
    city: str
    street: str
    number: str