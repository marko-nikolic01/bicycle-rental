from pydantic import BaseModel

class UserDetailsAddressDTO(BaseModel):
    country: str
    city: str
    street: str
    number: str
