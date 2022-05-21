from fastapi import FastAPI


def create_app() -> FastAPI:
    application = FastAPI()
    return application


app = create_app()


@app.get("/")
def index():
    return {"projectName": "star-gaze"}
