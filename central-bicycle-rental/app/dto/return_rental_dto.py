from pydantic import BaseModel
from uuid import UUID

class ReturnRentalDTO(BaseModel):
    national_id: str
    bike_id: UUID
