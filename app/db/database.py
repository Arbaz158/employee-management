# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# from app.core.config import settings
#
#
# engine = create_engine(
#     settings.DATABASE_URL,
#     pool_pre_ping=True,
# )
#
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )
#
#
# def get_db():
#     db = SessionLocal()
#
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


database_url = URL.create(
    drivername="mysql+pymysql",
    username=settings.DB_USERNAME,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)


engine = create_engine(
    database_url,
    pool_pre_ping=True,
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()