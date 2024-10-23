from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os.path
SQLALCHEMY_DATABASE_URL = "sqlite:///../data/titanic.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()