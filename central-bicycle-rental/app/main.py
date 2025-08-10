from fastapi import FastAPI
from .database import engine, Base
from app.controller import registration_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Central bicycle rental")

app.include_router(registration_router)