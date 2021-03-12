# schemas.py
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel


# データの作成および読み取りで使用する共通の属性
class WordBase(BaseModel):
    name: str


# データの作成時に使用 idといった作成時には不要なものを持たない
class WordCreate(WordBase):
    pass


# データ読み取り時に使用
class Word(WordBase):
    id: int
    tweeted_at: datetime
    created_at: datetime
    updated_at: datetime

    # ORMモードの使用を許可する
    class Config:
        orm_mode = True
