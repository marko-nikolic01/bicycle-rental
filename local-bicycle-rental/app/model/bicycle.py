import uuid
from sqlalchemy import Column, ForeignKey, Enum as PgEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base
from .enumeration import BicycleType

class Bicycle(Base):
    __tablename__ = "bicycles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(PgEnum(BicycleType), nullable=False)

    rental_record_id = Column(UUID(as_uuid=True), ForeignKey("rental_records.id"))
    rental_record = relationship("RentalRecord", uselist=False, back_populates="bicycle")
