from  pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    MAIL: str="dummy"
    MAIL_PASSWORD: SecretStr=SecretStr("dummy")
    MAIL_USERNAME: str="dummy"
    MAIL_FROM_NAME: str="dummy"

    model_config = SettingsConfigDict(
        env_file=".env",           # Read from a .env file
        env_file_encoding="utf-8"
    )

settings = Settings()