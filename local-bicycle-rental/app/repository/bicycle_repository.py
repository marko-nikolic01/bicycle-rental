from sqlalchemy.orm import Session
from typing import List
from app.model import Bicycle, BicycleType

class BicycleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id_and_type(self, id: str, type: BicycleType) -> Bicycle | None:
        return self.db.query(Bicycle).filter(
            Bicycle.id == id,
            Bicycle.type == type
        ).first()
    
    def get_all(self) -> List[Bicycle]:
        return self.db.query(Bicycle).all()

    def save(self, bicycle: Bicycle) -> Bicycle:
        self.db.add(bicycle)
        self.db.commit()
        self.db.refresh(bicycle)
        return bicycle
