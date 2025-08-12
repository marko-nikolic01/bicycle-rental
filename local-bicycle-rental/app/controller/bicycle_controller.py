from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.repository import BicycleRepository
from app.service import BicycleService
from app.dto import BicycleDetailsDTO

router = APIRouter(prefix="/api/bicycles", tags=["Bicycles"])

@router.get("/", response_model=List[BicycleDetailsDTO])
def get_all_bicycle_details(db: Session = Depends(get_db)):
    bicycle_repository = BicycleRepository(db)
    bicycle_service = BicycleService(bicycle_repository)
    return bicycle_service.get_all_bicycle_details()
