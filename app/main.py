from fastapi import FastAPI

from app.api.routers.ping import router as ping_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    """Создаёт и настраивает экземпляр FastAPI-приложения."""
    settings = get_settings()

    application = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    application.include_router(ping_router)

    return application


app = create_app()
