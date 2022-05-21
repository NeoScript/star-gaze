from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EventSchema(BaseModel):
    id: Optional[int]
    timestamp: datetime
    event_source: str
    event_type: str

    class Config:
        orm_mode = True
