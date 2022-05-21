import sqlalchemy
from config import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = settings.db_url
engine = sqlalchemy.create_engine(db_url, pool_pre_ping=True)
SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()
