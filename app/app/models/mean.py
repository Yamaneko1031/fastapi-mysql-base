# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.sqltypes import DATETIME

from app.db.database import Base


class Mean(Base):
    __tablename__ = 'means'
    id = Column(Integer, primary_key=True)
    text = Column(String(128),nullable=False)
    bad = Column(Integer, default=0)
    created_at = Column(DATETIME, server_default=current_timestamp(),nullable=False)
    updated_at = Column(DATETIME, server_default=current_timestamp(),nullable=False)
    word_id = Column(Integer, ForeignKey('words.id'),nullable=False)
