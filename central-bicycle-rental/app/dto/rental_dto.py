from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class RentalDTO(BaseModel):
    national_id: str
    bike_id: UUID
    rental_date: datetime
