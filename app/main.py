from fastapi import FastAPI


def create_app() -> FastAPI:
    """Создаёт и настраивает экземпляр FastAPI-приложения."""
    return FastAPI(
        title="Сервис кадастровых запросов",
        description=(
            "Асинхронный сервис для обработки кадастровых запросов "
            "и хранения истории результатов."
        ),
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )


app = create_app()