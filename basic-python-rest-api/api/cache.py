# api/cache.py
from redis import asyncio as aioredis
from fastapi import Request, Response
from functools import wraps

redis = aioredis.from_url("redis://localhost")

def cache_response(ttl: int = 60):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            cache_key = f"{request.url.path}:{str(request.query_params)}"
            cached = await redis.get(cache_key)
            
            if cached:
                return Response(content=cached, media_type="application/json")
            
            response = await func(request, *args, **kwargs)
            await redis.setex(cache_key, ttl, response.body)
            
            return response
        return wrapper
    return decorator