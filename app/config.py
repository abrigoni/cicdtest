from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Awesome API"
    ENV: str = "Development"
    DB_URL: str = ""

    class Config:
        env_file = '.env'
