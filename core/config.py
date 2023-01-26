import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = 'api/v1'
    VERSION: str
    SECRET_KEY: str = secrets.token_urlsafe(32)
    HOST: str
    PORT: int
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PWD: str
    POSTGRES_DB: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()

print(settings.dict())