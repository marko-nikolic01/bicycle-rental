from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.model import BicycleType

class RentalSuccessDTO(BaseModel):
    id: UUID
    national_id: str
    bicycle_id: UUID
    bicycle_type: BicycleType
    rental_date: datetime
