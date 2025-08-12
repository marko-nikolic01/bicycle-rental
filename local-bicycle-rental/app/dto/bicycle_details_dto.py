from pydantic import BaseModel
from uuid import UUID
from app.model import BicycleType

class BicycleDetailsDTO(BaseModel):
    id: UUID
    type: BicycleType
    can_rent: bool
