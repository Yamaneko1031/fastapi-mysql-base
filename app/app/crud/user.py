# crud.py
from sqlalchemy.orm import Session

import app.models
import app.schemas


def get_user(db: Session, user_id: int):
    return db.query(app.models.User).filter(app.models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(app.models.User).filter(app.models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(app.models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: app.schemas.UserCreate):
    db_user = app.models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
