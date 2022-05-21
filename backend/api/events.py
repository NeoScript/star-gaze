from fastapi import APIRouter, Depends
from models.events import EventTable
from sqlalchemy.orm import Session

from api.deps import get_db

router = APIRouter(prefix="/events")


@router.get("")
def list_events(db: Session = Depends(get_db)):
    results = db.query(EventTable).all()
    return results
