from fastapi import HTTPException, status
from typing import List
from app.repository import BicycleRepository
from app.dto import BicycleDetailsDTO

class BicycleService:
    def __init__(self, bicycle_repository: BicycleRepository):
        self.bicycle_repository = bicycle_repository
    
    def get_all_bicycle_details(self) -> List[BicycleDetailsDTO]:
        bicycle_details = []

        bicycles = self.bicycle_repository.get_all()
        for bicycle in bicycles:
            bicycle_details.append(
                BicycleDetailsDTO(
                    id=bicycle.id,
                    type=bicycle.type,
                    can_rent=bicycle.can_rent()
                )
            )

        return bicycle_details
