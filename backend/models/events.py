from db.session import Base
from sqlalchemy import Column, DateTime, Identity, Integer, Text


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, Identity(always=True), primary_key=True)

    timestamp = Column(DateTime(timezone=True))
    event_source = Column(Text)
    event_type = Column(Text)
