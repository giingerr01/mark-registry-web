from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:mahima@localhost:5432/mark_registry"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_database():
    """Dependency for getting a database session in routes"""
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
