import pytest
from pydantic import ValidationError

from app.core.config import Settings


def test_settings_have_expected_defaults() -> None:
    """Проверяет значения конфигурации по умолчанию."""
    settings = Settings(_env_file=None)

    assert settings.app_name == "Сервис кадастровых запросов"
    assert settings.app_version == "0.1.0"
    assert settings.app_host == "0.0.0.0"
    assert settings.app_port == 8000
    assert settings.log_level == "INFO"


def test_settings_accept_explicit_values() -> None:
    """Проверяет возможность явного переопределения настроек."""
    settings = Settings(
        app_name="Тестовый сервис",
        app_port=9000,
        log_level="DEBUG",
        _env_file=None,
    )

    assert settings.app_name == "Тестовый сервис"
    assert settings.app_port == 9000
    assert settings.log_level == "DEBUG"


@pytest.mark.parametrize("invalid_port", [0, 65536])
def test_settings_reject_invalid_port(invalid_port: int) -> None:
    """Проверяет отклонение недопустимого сетевого порта."""
    with pytest.raises(ValidationError):
        Settings(
            app_port=invalid_port,
            _env_file=None,
        )
