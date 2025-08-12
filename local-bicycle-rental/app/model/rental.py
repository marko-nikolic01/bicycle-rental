import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String(13), nullable=False)
    rental_date = Column(DateTime, default=datetime.utcnow)
    rental_end_date = Column(DateTime, nullable=True)

    rental_record_id = Column(UUID(as_uuid=True), ForeignKey("rental_records.id"))
    rental_record = relationship("RentalRecord", back_populates="rentals")

    def is_active(self) -> bool:
        return self.rental_end_date is None or self.rental_end_date > datetime.utcnow()