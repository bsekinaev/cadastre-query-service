from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping_returns_service_status() -> None:
    """Проверяет успешный ответ эндпоинта состояния сервиса."""
    response = client.get("/ping")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status": "ok",
        "service": "Сервис кадастровых запросов",
    }
