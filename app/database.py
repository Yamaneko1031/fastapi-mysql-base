# database.py
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
SQLALCHEMY_DATABASE_URL = sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username="tori",
            password="Yamanekoubou1031",
            database="test_database",
            query={
                "unix_socket": "{}/{}".format(
                    "/cloudsql",  # e.g. "/cloudsql"
                    "tori-304112:asia-northeast1:tori-db")  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
            }
        )
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://%s:%s@/%s?%s' % (
#     "tori",
#     "Yamanekoubou1031",
#     # "172.24.48.3:3306"
#     # "tori-304112:asia-northeast1:tori-db"
#     # "172.18.0.3:3306",
#     "test_database",
#     "unix_socket=/cloudsql/tori-304112:asia-northeast1:tori-db"
# )
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# サポートしているDBと対話するためのエンジン
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# DBに接続するためのセッション作成
SessionLocal = sessionmaker(bind=engine)

# declarativeメタクラス
Base = declarative_base()
