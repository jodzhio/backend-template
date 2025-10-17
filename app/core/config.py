from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    db_user: str
    db_pass: str
    db_host: str
    db_port: int
    db_base: str

    redis_user: str
    redis_user_password: str
    redis_password: str

    model_config = SettingsConfigDict(env_file=".env.example")
    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_base}"

settings = Settings()
