# models.py
from sqlalchemy import Column, Integer, String

from app.db.database import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    email = Column(String(64), unique=True, index=True)
