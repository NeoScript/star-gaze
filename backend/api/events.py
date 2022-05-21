from typing import List

from fastapi import APIRouter, Depends
from models.events import Events
from schemas.event_schema import EventSchema
from sqlalchemy.orm import Session

from api.deps import get_db

router = APIRouter(prefix="/events")


@router.get("", response_model=List[EventSchema])
def list_events(db: Session = Depends(get_db)):
    results = db.query(Events).all()
    return results


@router.post("", response_model=EventSchema)
def post_event(event: EventSchema, db: Session = Depends(get_db)):

    new_event = Events(**event.dict())

    db.add(new_event)
    db.commit()

    db.refresh(new_event)

    return new_event
