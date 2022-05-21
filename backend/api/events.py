from fastapi import APIRouter

router = APIRouter(prefix="/events")


@router.get("")
def list_events():
    return ["event1", "event2"]
