from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_PREFIX: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade"

    class Config:
        case_sensitive = True


settings = Settings()