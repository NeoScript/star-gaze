import sqlalchemy
from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def db_url(self):
        db_config = {
            "drivername": "postgresql+psycopg2",
            "username": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "database": self.POSTGRES_DB,
        }

        db_config["host"] = self.DB_HOST
        db_config["port"] = self.DB_PORT

        url = sqlalchemy.engine.URL.create(**db_config)

        return url


settings = Settings()
