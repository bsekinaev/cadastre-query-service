from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.core.config import Settings, get_settings
from app.schemas.ping import PingResponse

router = APIRouter(tags=["Состояние сервиса"])


@router.get(
    "/ping",
    response_model=PingResponse,
    status_code=status.HTTP_200_OK,
    summary="Проверить доступность сервиса",
    description="Возвращает успешный ответ, если HTTP-сервис запущен.",
)
async def ping(
    settings: Annotated[Settings, Depends(get_settings)],
) -> PingResponse:
    """Возвращает текущее состояние основного сервиса."""
    return PingResponse(
        status="ok",
        service=settings.app_name,
    )
