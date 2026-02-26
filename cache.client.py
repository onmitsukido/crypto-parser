import redis.asyncio as redis
from config import Config

redis_client = redis.from_url(Config.REDIS_URL, decode_responses=True)

async def set_price(coin: str, currency: str, price: str | float | int, ttl: int | None = None):

    key = f"price:{coin}:{currency}"
    actual_ttl = ttl if ttl is not None else Config.CACHE_TTL

    await redis_client.setex(key, actual_ttl, str(price))

async def get_price(coin: str, currency: str) -> str | None:

    key = f"price:{coin}:{currency}"
    
    return await redis_client.get(key)