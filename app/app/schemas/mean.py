# schemas.py
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel


# データの作成および読み取りで使用する共通の属性
class MeanBase(BaseModel):
    text: str


# データの作成時に使用 idといった作成時には不要なものを持たない
class MeanCreate(MeanBase):
    pass


# データ読み取り時に使用
class Mean(MeanBase):
    id: int
    bad: int
    created_at: datetime
    updated_at: datetime
    word_id: int

    # ORMモードの使用を許可する
    class Config:
        orm_mode = True
