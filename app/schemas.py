# schemas.py
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean


# データの作成および読み取りで使用する共通の属性
class UserBase(BaseModel):
    name: str
    email: str


# データの作成時に使用 idといった作成時には不要なものを持たない
class UserCreate(UserBase):
    pass


# データ読み取り時に使用
class User(UserBase):
    id: int

    # ORMモードの使用を許可する
    class Config:
        orm_mode = True


class TimeTest(BaseModel):
    id: int
    kind: str
    created_at: datetime

    # ORMモードの使用を許可する
    class Config:
        orm_mode = True
