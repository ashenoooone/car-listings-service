import os
from dataclasses import dataclass


@dataclass
class Settings:
    telegram_bot_token: str
    database_url: str
    openai_api_key: str | None
    openai_model: str
    max_results: int = 10


def _build_async_database_url(raw_url: str) -> str:
    """
    Docker-compose пробрасывает DATABASE_URL в виде postgres://...
    Для async SQLAlchemy нужен драйвер asyncpg.
    """
    if raw_url.startswith("postgresql+asyncpg://"):
        return raw_url
    if raw_url.startswith("postgresql://"):
        return raw_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    if raw_url.startswith("postgres://"):
        return raw_url.replace("postgres://", "postgresql+asyncpg://", 1)
    return raw_url


def get_settings() -> Settings:
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL is not set")

    openai_api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    return Settings(
        telegram_bot_token=bot_token,
        database_url=_build_async_database_url(db_url),
        openai_api_key=openai_api_key,
        openai_model=model,
    )

