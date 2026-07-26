from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Хранит и валидирует конфигурацию приложения."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Сервис кадастровых запросов"
    app_description: str = (
        "Асинхронный сервис для обработки кадастровых запросов и хранения истории результатов."
    )
    app_version: str = "0.1.0"

    app_host: str = "0.0.0.0"
    app_port: int = Field(default=8000, ge=1, le=65535)

    log_level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ] = "INFO"


@lru_cache
def get_settings() -> Settings:
    """Возвращает общий экземпляр настроек приложения."""
    return Settings()
