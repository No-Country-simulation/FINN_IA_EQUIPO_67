from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@db:5432/finn"
    PROJECT_NAME: str = "finn-backend"
    FIREBASE_PROJECT_ID: str = ""
    FIREBASE_CREDENTIALS: str | None = None  # ruta al service account JSON
    FIREBASE_CREDENTIALS_JSON: str | None = None  # json crudo del service account
    ENVIRONMENT: str = "development"
    PYTHON_VERSION: str = "3.12"

    class Config:
        env_file = ".env"

settings = Settings()
