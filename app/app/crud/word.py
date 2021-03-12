# word.py
from sqlalchemy.orm import Session

import app.models
import app.schemas


def get_word(db: Session, name: str):
    return db.query(app.models.Word).filter(app.models.Word.name == name).first()


def get_words(db: Session, skip: int = 0, limit: int = 100):
    return db.query(app.models.Word).offset(skip).limit(limit).all()


def create_word(db: Session, word: app.schemas.WordCreate):
    db_word = app.models.Word(name=word.name)
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word
