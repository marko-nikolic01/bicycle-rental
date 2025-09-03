import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_HOST = os.getenv("DATABASE_HOST", "local-bicycle-rental-database-ns")
DATABASE_PORT = os.getenv("DATABASE_PORT", 5432)
DATABASE_NAME = os.getenv("DATABASE_NAME", "local-bicycle-rental-ns")
DATABASE_URL = f'postgresql://postgres:postgres@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def seed_bicycles():
    from .model import Bicycle
    from .model import BicycleType

    db = SessionLocal()
    try:
        count = db.query(Bicycle).count()
        if count == 0:
            print("Seeding bicycle data...")
            bicycles = []
            for bicycle_type in BicycleType:
                for _ in range(5):
                    bicycles.append(Bicycle(type=bicycle_type))
            db.add_all(bicycles)
            db.commit()
        else:
            print("Skipping seeding bicycle data...")
    finally:
        db.close()