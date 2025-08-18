from fastapi import FastAPI
from app.database import engine, Base
from app.controller import registration_router, rental_router, user_router

def create_app():
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="Central bicycle rental")

    app.include_router(registration_router)
    app.include_router(rental_router)
    app.include_router(user_router)

    return app

app = create_app()
