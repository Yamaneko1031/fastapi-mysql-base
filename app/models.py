# models.py
import datetime

from sqlalchemy import Column, Integer, String, Time
# from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.sql.functions import current_timestamp

from database import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(32))
    email = Column('email', String, unique=True, index=True)


class TimeStamp(Base):
    __tablename__ = 'timestamps'
    id = Column('id', Integer, primary_key=True)
    kind = Column('kind', String)
    created_at = Column('created_at', String, server_default=current_timestamp(),nullable=False)


if __name__ == "__main__":
    print("run models.py")
    Base.metadata.create_all(bind=engine)
