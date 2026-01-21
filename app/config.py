from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Awesome API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DESCRIPTION: str = "Dashboard untuk monitoring IoT devices"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache()
def get_settings():
    return Settings()
