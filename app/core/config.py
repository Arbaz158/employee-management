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

# from pydantic_settings import BaseSettings, SettingsConfigDict
#
#
# class Settings(BaseSettings):
#
#     DATABASE_URL: str
#
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )
#
#
# settings = Settings()


from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()