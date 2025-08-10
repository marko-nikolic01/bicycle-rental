from .registration_controller import router as registration_router
from .rental_controller import router as rental_router
from .user_controller import router as user_router

__all__ = [
    "registration_router",
    "rental_router",
    "user_router"
]
