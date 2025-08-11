from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ReturnRentalSuccessDTO(BaseModel):
    id: UUID
    national_id: str
    bicycle_id: UUID
    rental_date: datetime
    rental_end_date: datetime
