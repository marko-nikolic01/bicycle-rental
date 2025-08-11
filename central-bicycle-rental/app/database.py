import os
import time
import sqlalchemy.exc
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_HOST = os.getenv("DATABASE_HOST", "central-bicycle-rental-database")
DATABASE_PORT = os.getenv("DATABASE_PORT", 5432)
DATABASE_NAME = os.getenv("DATABASE_NAME", "central-bicycle-rental")
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
