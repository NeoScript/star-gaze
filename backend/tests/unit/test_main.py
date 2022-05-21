from fastapi import FastAPI
from main import create_app


def test_app_creation():
    result = create_app()

    assert isinstance(result, FastAPI)
