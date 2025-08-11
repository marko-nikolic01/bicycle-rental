import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .rental_record import RentalRecord
from .rental import Rental
from ..database import Base

class Bicycle(Base):
    __tablename__ = "bicycles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    rental_record_id = Column(UUID(as_uuid=True), ForeignKey("rental_records.id"))
    rental_record = relationship("RentalRecord", uselist=False, back_populates="bicycle")
