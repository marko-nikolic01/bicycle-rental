import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
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
