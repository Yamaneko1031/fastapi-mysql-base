# database.py
import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


def get_db_url():
    return sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        host=os.environ['MYSQL_HOST'],
        port="3306",
        database=os.environ['MYSQL_DATABASE'],
        query={'charset': 'utf8'}
    )

# サポートしているDBと対話するためのエンジン
engine = create_engine(get_db_url())

# DBに接続するためのセッション作成
SessionLocal = sessionmaker(bind=engine)

# declarativeメタクラス
Base = declarative_base()
