# from pydantic_settings import BaseSettings
#
#
# class Settings(BaseSettings):
#     DATABASE_URL: str
#
#     class Config:
#         env_file = ".env"
#
#
# settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()