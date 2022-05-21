from typing import Generator

from db.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    yield db
    db.close()
