from fastapi import FastAPI
import time
from app.database import engine, Base
from app.controller import registration_router, rental_router, user_router

def create_app():
    max_retries = 20
    retry_interval = 2
    for attempt in range(max_retries):
        try:
            Base.metadata.create_all(bind=engine)
            print("Database ready...")
            break
        except Exception as e:
            print(f"Database not ready, retrying in {retry_interval}s... ({attempt+1}/{max_retries})")
            time.sleep(retry_interval)
    else:
        raise RuntimeError("Could not connect to the database after multiple attempts.")

    app = FastAPI(title="Central bicycle rental")

    app.include_router(registration_router)
    app.include_router(rental_router)
    app.include_router(user_router)
    
    return app

app = create_app()
