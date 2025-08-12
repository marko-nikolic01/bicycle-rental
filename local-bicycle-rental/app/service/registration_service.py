import requests
import os
from fastapi.responses import JSONResponse
from app.dto import RegistrationDTO

class RegistrationService:
    def __init__(self):
        CENTRAL_BICYCLE_RENTAL_HOST = os.getenv("CENTRAL_BICYCLE_RENTAL_HOST", "central-bicycle-rental")
        CENTRAL_BICYCLE_RENTAL_PORT = os.getenv("CENTRAL_BICYCLE_RENTAL_PORT", 8000)
        self.CENTRAL_BICYCLE_RENTAL_URL = f"http://{CENTRAL_BICYCLE_RENTAL_HOST}:{CENTRAL_BICYCLE_RENTAL_PORT}/api"

    def register(self, registration_dto: RegistrationDTO):
        response = requests.post(
            f"{self.CENTRAL_BICYCLE_RENTAL_URL}/users",
            json=registration_dto.dict()
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
