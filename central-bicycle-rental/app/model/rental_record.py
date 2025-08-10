import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base

class RentalRecord(Base):
    __tablename__ = "rental_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    rentals = relationship("Rental", back_populates="rental_record", cascade="all, delete-orphan")
    user = relationship("User", back_populates="rental_record", uselist=False)
