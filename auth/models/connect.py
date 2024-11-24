import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_URL = os.getenv("URL_DB")


engine = create_engine(
    SQLALCHEMY_URL
)


LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()