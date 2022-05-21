from fastapi import FastAPI

from api.events import router as events_endpoint
from config import settings
from db.session import Base, engine

try:
    print("creating db tables")
    Base.metadata.create_all(engine)
except:
    print("failed to init db")


def create_app() -> FastAPI:
    application = FastAPI()

    application.include_router(events_endpoint)
    return application


app = create_app()


@app.get("/")
def index():
    print(settings)
    return {"projectName": "star-gaze"}
