from fastapi import FastAPI

from api.events import router as events_endpoint
from config import settings


def create_app() -> FastAPI:
    application = FastAPI()

    application.include_router(events_endpoint)
    return application


app = create_app()


@app.get("/")
def index():
    print(settings)
    return {"projectName": "star-gaze"}
