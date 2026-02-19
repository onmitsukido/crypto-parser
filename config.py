from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    COINGECKO_API_URL = os.getenv("COINGECKO_API_URL")
    REDIS_URL = os.getenv("REDIS_URL")
    CACHE_TTL = int(os.getenv("CACHE_TTL"))

    if not COINGECKO_API_URL:
        raise ValueError("COINGECKO_API_URL is required")
    if not REDIS_URL:
        raise ValueError("REDIS_URL is required")
    try:
        CACHE_TTL = int(CACHE_TTL)
    except (TypeError, ValueError):
        raise ValueError("CACHE_TTL must be an integer")