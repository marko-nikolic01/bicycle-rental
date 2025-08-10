import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(String, nullable=False)

    user = relationship("User", back_populates="address")
