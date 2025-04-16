from pydantic import BaseSettings, AnyUrl, RedisDsn
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Example API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: AnyUrl = "postgresql+asyncpg://postgres:postgres@localhost:5432/example"
    SYNC_DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/example"
    
    # Security
    SECRET_KEY: str = "secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Redis
    REDIS_URL: Optional[RedisDsn] = None
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()