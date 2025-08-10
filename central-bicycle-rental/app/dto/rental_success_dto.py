from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class RentalSuccessDTO(BaseModel):
    id: UUID
    national_id: str
    bike_id: UUID
    rental_date: datetime
