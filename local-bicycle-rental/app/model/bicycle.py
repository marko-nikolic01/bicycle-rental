import uuid
from sqlalchemy import Column, ForeignKey, Enum as PgEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base
from .enumeration import BicycleType
from .rental import Rental
from .rental_record import RentalRecord

class Bicycle(Base):
    __tablename__ = "bicycles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(PgEnum(BicycleType), nullable=False)

    rental_record_id = Column(UUID(as_uuid=True), ForeignKey("rental_records.id"))
    rental_record = relationship("RentalRecord", uselist=False, back_populates="bicycle")

    def can_rent(self):
        return not self.rental_record or not self.rental_record.has_active_rental()
    
    def add_rental(self, rental: Rental):
        if not self.rental_record:
            self.rental_record = RentalRecord()
        self.rental_record.add_rental(rental)

    def return_rental(self):
        return self.rental_record.return_rental()
