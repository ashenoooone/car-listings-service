from functools import lru_cache
from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    app_name: str = "Car Listings Service"
    secret_key: str = "CHANGE_ME_SECRET"  
    database_url: AnyUrl = "postgresql+asyncpg://user:password@localhost:5432/car_listings"
    jwt_lifetime_seconds: int = 60 * 60 * 24

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()

