import logging
from logging.config import dictConfig
from pathlib import Path
from ..config.settings import settings

def configure_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": settings.LOG_FORMAT,
                "datefmt": "%Y-%m-%d %H:%M:%S"
            },
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "fmt": "%(asctime)s %(name)s %(levelname)s %(message)s"
            }
        },
        "handlers": {
            "console": {
                "level": settings.LOG_LEVEL,
                "class": "logging.StreamHandler",
                "formatter": "standard"
            },
            "file": {
                "level": settings.LOG_LEVEL,
                "class": "logging.handlers.RotatingFileHandler",
                "filename": log_dir / "api.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "formatter": "json",
                "encoding": "utf8"
            }
        },
        "loggers": {
            "": {
                "handlers": ["console", "file"],
                "level": settings.LOG_LEVEL,
                "propagate": True
            },
            "uvicorn.error": {
                "level": settings.LOG_LEVEL
            },
            "uvicorn.access": {
                "level": settings.LOG_LEVEL,
                "handlers": ["console", "file"],
                "propagate": False
            }
        }
    }
    
    dictConfig(logging_config)