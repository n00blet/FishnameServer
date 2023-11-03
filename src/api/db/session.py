from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.api.core.config import settings

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:rakshith@localhost:5432/fishnames"
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = None
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        # Handle initialization exceptions
        print(f"Error during database session initialization: {e}")
    finally:
        if db:
            db.close()
