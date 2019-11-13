"""
SQLAlchemy setup
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# test.db file in current directory
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# connect_args is needed only for SQLite. It's not needed for other databases.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionMaker()
