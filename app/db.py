from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import config


engine = create_engine(
        config.settings.database_uri, connect_args={"check_same_thread": False}
        )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from app import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
