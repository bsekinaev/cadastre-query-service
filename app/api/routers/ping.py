from fastapi import APIRouter, status

from app.schemas.ping import PingResponse

router = APIRouter(tags=["Состояние сервиса"])


@router.get(
    "/ping",
    response_model=PingResponse,
    status_code=status.HTTP_200_OK,
    summary="Проверить доступность сервиса",
    description=(
        "Возвращает успешный ответ, если HTTP-сервис запущен и способен принимать запросы."
    ),
)
async def ping() -> PingResponse:
    """Возвращает текущее состояние основного сервиса."""
    return PingResponse(
        status="ok",
        service="Сервис кадастровых запросов",
    )
