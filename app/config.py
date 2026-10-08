from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_HOSTNAME: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_PASSWORD: str = "password"
    DATABASE_NAME: str = "fastapi"
    DATABASE_USERNAME: str = "postgres"
    SECRET_KEY: str = "development-only-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()