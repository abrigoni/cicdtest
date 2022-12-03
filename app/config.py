from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Awesome API"
    ENV: str = "Development"

    class Config:
        env_file = '.env'
