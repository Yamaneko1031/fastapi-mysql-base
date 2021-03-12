# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.sqltypes import DATETIME
from sqlalchemy.orm import relationship

from app.db.database import Base


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    tweeted_at = Column(DATETIME, server_default=current_timestamp(),nullable=False)
    created_at = Column(DATETIME, server_default=current_timestamp(),nullable=False)
    updated_at = Column(DATETIME, server_default=current_timestamp(),nullable=False)
    means = relationship("Mean", backref="words")
