from fastapi import FastAPI
from app.database import engine, Base
from app.controller import registration_router, rental_router, user_router
import httpx
from fastapi import APIRouter

def create_app():
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="Central bicycle rental")

    app.include_router(registration_router)
    app.include_router(rental_router)
    app.include_router(user_router)

        # Egress test router
    test_router = APIRouter()

    @test_router.get("/test-egress")
    async def test_egress():
        try:
            r = httpx.get("https://google.com", timeout=5)
            return {"status": "success", "code": r.status_code}
        except Exception as e:
            return {"status": "blocked", "error": str(e)}

    app.include_router(test_router)

    return app

app = create_app()
