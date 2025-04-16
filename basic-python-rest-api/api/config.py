from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "API Modernizada"
    PROJECT_DESCRIPTION: str = "API renovada do projeto antigo"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Logging
    LOG_FILENAME: str = "api.log"
    
    # Docs
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    class Config:
        env_file = ".env"

settings = Settings()