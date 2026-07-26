from typing import Literal

from pydantic import BaseModel, Field


class PingResponse(BaseModel):
    """Описывает ответ проверки доступности сервиса."""

    status: Literal["ok"] = Field(
        description="Текущее состояние сервиса.",
        examples=["ok"],
    )
    service: str = Field(
        description="Отображаемое название сервиса.",
        examples=["Сервис кадастровых запросов"],
    )
