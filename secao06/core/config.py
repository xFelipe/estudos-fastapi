from pydantic_config import SettingsModel
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from typing import Any


__UMA_SEMANA_EM_MINUTOS = 60 * 24 * 7

class Settings(SettingsModel):
    API_V1_PREFIX: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade"
    DBBaseModel: DeclarativeMeta = declarative_base()

    # import secrets
    # token: str = secrets.token_urlsafe(32)
    JWT_SECRET: str = "Wybx-QnsC6ioT6VLzYMUBjnyssU7y0fMEKtzA4D-NgQ"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRES_MINUTES: int = __UMA_SEMANA_EM_MINUTOS

    class Config:
        case_sensitive = True


settings = Settings()
