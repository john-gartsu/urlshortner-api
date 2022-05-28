from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_settings

# db entry point
engine = create_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}
)

# create working db session
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# connects to db engine to the SQLAlchemy functionality of models
Base = declarative_base()