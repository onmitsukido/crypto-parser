import httpx
from config import Config
from logger import get_logger

logger = get_logger(__name__)

async def fetch_prices(coins: list[str], currencies: list[str]):
    
    url = f"{Config.COINGECKO_API_URL}/simple/price"
    params = {
        "ids": ",".join(coins),
        "vs_currencies": ",".join(currencies)
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        logger.debug(f"Данные из CoinGecko получены")
        return response.json()