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
    redis_host: str
    redis_port: int

    model_config = SettingsConfigDict(env_file=".env")
    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_base}"

    @property
    def REDIS_URL(self) -> str:
        if self.redis_user and self.redis_user_password:
            return f"redis://{self.redis_user}:{self.redis_user_password}@{self.redis_host}:{self.redis_port}/0"
        elif self.redis_password:
            return f"redis://:{self.redis_password}@{self.redis_host}:{self.redis_port}/0"
        else:
            return f"redis://{self.redis_host}:{self.redis_port}/0"

settings = Settings()
