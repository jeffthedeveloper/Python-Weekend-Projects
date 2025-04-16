# __init__.py - Versão atualizada

import logging
from logging.handlers import RotatingFileHandler
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path
from .config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
)

# Configuração de CORS (ajuste conforme necessidade)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração de logging melhorada
def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    formatter = logging.Formatter(
        "[%(asctime)s] [%(process)d] [%(levelname)s] "
        "%(module)s.%(funcName)s:%(lineno)d - %(message)s"
    )
    
    # File handler com rotação
    file_handler = RotatingFileHandler(
        log_dir / settings.LOG_FILENAME,
        maxBytes=10_000_000,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
    console_handler.setFormatter(formatter)
    
    # Configuração do logger principal
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    # Remove handlers duplicados (comum em reload)
    while logger.hasHandlers() and len(logger.handlers) > 2:
        logger.removeHandler(logger.handlers[0])

# Chama a configuração de logging
setup_logging()

# Tratamento de erros global
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"detail": "Recurso não encontrado"},
    )

# Importação de rotas (usando routers do FastAPI)
from .routers import examples, items, users

app.include_router(examples.router)
app.include_router(items.router)
app.include_router(users.router)

# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}