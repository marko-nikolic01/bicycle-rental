from .registration_controller import router as registration_router
from .rental_controller  import router as rental_router
from .bicycle_controller  import router as bicycle_router

__all__ = [
    "registration_router",
    "rental_router",
    "bicycle_router"
]
