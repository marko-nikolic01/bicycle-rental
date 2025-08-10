from sqlalchemy.orm import Session
from typing import List
from app.model import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_national_id(self, national_id: str) -> User | None:
        return self.db.query(User).filter(User.national_id == national_id).first()
    
    def get_all(self) -> List[User]:
        return self.db.query(User).all()

    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
