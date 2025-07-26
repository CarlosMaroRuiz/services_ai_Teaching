import os
from pydantic_settings import BaseSettings
import multiprocessing

class Settings(BaseSettings):
    APP_NAME: str = "Interview Agent API"
    API_PREFIX: str = "/api/v1"
    WORKERS: int = int(os.getenv("WORKERS", multiprocessing.cpu_count() * 2 + 1))

settings = Settings()