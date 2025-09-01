from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./wallet.db"

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session local = like a "session with the database"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all our models (tables)
Base = declarative_base()
