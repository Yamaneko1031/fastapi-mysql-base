# mean.py
from sqlalchemy.orm import Session

import app.models
import app.schemas


def get_means(db: Session, skip: int = 0, limit: int = 100):
    return db.query(app.models.Mean).offset(skip).limit(limit).all()


def create_mean(db: Session, mean: app.schemas.MeanCreate, owner_word: str):
    set_word_id = db.query(app.models.Word).filter(app.models.Word.name == owner_word).first().id
    db_mean = app.models.Mean(text=mean.text, word_id=set_word_id)
    db.add(db_mean)
    db.commit()
    db.refresh(db_mean)
    return db_mean
