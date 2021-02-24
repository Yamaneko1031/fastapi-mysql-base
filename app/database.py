# database.py
import os
from typing import Any

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.ext.declarative import as_declarative, declared_attr


from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"

# SQLALCHEMY_DATABASE_URL = sqlalchemy.engine.url.URL(
#             drivername="mysql+pymysql",
#             username="tori",
#             password="Yamanekoubou1031",
#             database="test_database",
#             query={
#                 "unix_socket": "{}/{}".format(
#                     "/cloudsql",  # e.g. "/cloudsql"
#                     "tori-304112:asia-northeast1:tori-db")  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
#             }
#         )

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
#     "tori",
#     "Yamanekoubou1031",
#     # "172.24.48.3:3306"
#     # "tori-304112:asia-northeast1:tori-db"
#     "172.24.48.3:3306",
#     # "127.0.0.1:3306"
#     "test_database",
#     # "unix_socket=/cloudsql/tori-304112:asia-northeast1:tori-db"
# )

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8'.format(
#     "tori",
#     "Yamanekoubou1031",
#     # "172.24.48.3:3306"
#     # "tori-304112:asia-northeast1:tori-db"
#     "172.24.48.3:1433",
#     # "127.0.0.1:3306"
#     "test_database",
#     # "unix_socket=/cloudsql/tori-304112:asia-northeast1:tori-db"
# )

# SQLALCHEMY_DATABASE_URL = sqlalchemy.engine.url.URL(
#         drivername="mysql+pymysql",
#         username="tori",  # e.g. "my-database-user"
#         password="Yamanekoubou1031",  # e.g. "my-database-password"
#         host="172.24.48.3",  # e.g. "127.0.0.1"
#         port="3306",  # e.g. 3306
#         database="test_database",  # e.g. "my-database-name"
#     )

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
# @as_declarative()
# class Base:
#     id: Any
#     __name__: str
#     # Generate __tablename__ automatically
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()