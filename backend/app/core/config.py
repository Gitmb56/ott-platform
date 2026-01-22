import os
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "OTT Platform"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost/ott_platform"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()