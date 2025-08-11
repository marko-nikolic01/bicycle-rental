from fastapi import FastAPI
from app.model import Bicycle
from app.database import engine, Base, seed_bicycles
from app.controller import registration_router

def create_app():
    Base.metadata.create_all(bind=engine)
    seed_bicycles()

    app = FastAPI(title="Local bicycle rental")

    app.include_router(registration_router)
    
    return app

app = create_app()
