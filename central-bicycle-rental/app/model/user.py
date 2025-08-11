import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .rental_record import RentalRecord
from .rental import Rental
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    national_id = Column(String(13), unique=True, nullable=False)

    address_id = Column(UUID(as_uuid=True), ForeignKey("addresses.id"))
    address = relationship("Address", uselist=False, back_populates="user")

    rental_record_id = Column(UUID(as_uuid=True), ForeignKey("rental_records.id"))
    rental_record = relationship("RentalRecord", uselist=False, back_populates="user")

    def count_active_rentals(self) -> int:
        if not self.rental_record:
            return 0
        return self.rental_record.count_active_rentals()

    def add_rental(self, rental: Rental):
        if not self.rental_record:
            self.rental_record = RentalRecord()
        self.rental_record.add_rental(rental)

    def get_rental(self, bicycle_id: UUID):
        return self.rental_record.get_rental(bicycle_id)
    
    def return_rental(self, bicycle_id):
        return self.rental_record.return_rental(bicycle_id)
