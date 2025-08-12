import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base
from .rental import Rental

class RentalRecord(Base):
    __tablename__ = "rental_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    rentals = relationship("Rental", back_populates="rental_record", cascade="all, delete-orphan")
    bicycle = relationship("Bicycle", back_populates="rental_record", uselist=False)

    def has_active_rental(self):
        for rental in self.rentals:
            if rental.is_active():
                return True
        return False
    
    def add_rental(self, rental: Rental):
        self.rentals.append(rental)
