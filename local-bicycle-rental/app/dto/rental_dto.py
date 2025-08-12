from pydantic import BaseModel, constr
from uuid import UUID
from datetime import datetime
from app.model import BicycleType

class RentalDTO(BaseModel):
    national_id: constr(min_length=13, max_length=13)
    bicycle_id: UUID
    bicycle_type: BicycleType
    rental_date: datetime
