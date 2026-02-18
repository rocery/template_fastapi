from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    APP_NAME: str = "Awesome API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DESCRIPTION: str = "Dashboard untuk monitoring IoT devices"

    # Get From .env file
    DATABASE_URL_iot: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def DATABASE_URL_iot(self) -> str:
        if self.DATABASE_URL_iot:
            return self.DATABASE_URL_iot

        return (
            f"mysql+aiomysql://"
            f"{self.DB_USER_iot}:"
            f"{self.DB_PASSWORD_iot}@"
            f"{self.DB_HOST_iot}:"
            f"{self.DB_PORT_iot}/"
            f"{self.DB_NAME_iot}"
        )

@lru_cache()
def get_settings():
    return Settings()
