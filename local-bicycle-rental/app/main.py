from fastapi import FastAPI
from app.model import Bicycle, BicycleType
from app.database import engine, Base, seed_bicycles

def create_app():
    Base.metadata.create_all(bind=engine)
    seed_bicycles()

    app = FastAPI(title="Local bicycle rental")
    
    return app

app = create_app()
