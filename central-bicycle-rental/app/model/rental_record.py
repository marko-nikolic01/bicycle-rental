import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .rental import Rental
from ..database import Base

class RentalRecord(Base):
    __tablename__ = "rental_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    rentals = relationship("Rental", back_populates="rental_record", cascade="all, delete-orphan")
    user = relationship("User", back_populates="rental_record", uselist=False)

    def count_active_rentals(self) -> int:
        return sum(1 for rental in self.rentals if rental.is_active())
    
    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def get_rental(self, bike_id: UUID):
        for rental in self.rentals:
            if rental.bike_id == bike_id and rental.is_active():
                return rental
        return None

    def return_rental(self, bike_id):
        rental = self.get_rental(bike_id)
        if rental:
            rental.return_rental()
        return rental
