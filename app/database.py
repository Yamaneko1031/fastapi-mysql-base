# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    "tori",
    "Yamanekoubou1031",
    "127.0.0.1:3306"
    # "tori-304112:asia-northeast1:tori-db"
    # "172.18.0.3:3306",
    "test_database",
)
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# サポートしているDBと対話するためのエンジン
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# DBに接続するためのセッション作成
SessionLocal = sessionmaker(bind=engine)

# declarativeメタクラス
Base = declarative_base()
