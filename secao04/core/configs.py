from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import Any


class Settings(BaseSettings):
    """Configurações gerais usadas na aplicação"""
    API_V1_PREFIX: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade"
    DBBaseModel: Any = declarative_base()

    class Config:
        case_sensitive = True



settings = Settings()