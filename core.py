from typing import Dict, List
from price_fetcher import fetch_prices
from cache_client import get_price, set_price
from logger import get_logger

logger = get_logger(__name__)

async def get_prices_with_cache(coins: List[str], currencies: List[str]) -> Dict[str, Dict[str, str]]:
    all_cached = True
    result: dict[str, dict[str, str]] = {}

    for coin in coins:
        result[coin] = {}
        for currency in currencies:
            cached_value = await get_price(coin, currency)
            if cached_value is None:
                all_cached = False
            result[coin][currency] = cached_value

    if all_cached:
        logger.info(f"Все данные получены из кэша")
        return result
    else:
        logger.info(f"Запрашиваем свежие данные у CoinGecko...")

    fresh_data: dict = await fetch_prices(coins, currencies)

    for coin in coins:
        for currency in currencies:
            price_value = fresh_data[coin][currency]
            await set_price(coin, currency, price_value)

    final_result: dict[str, dict[str, str]] = {}
    for coin in coins:
        final_result[coin] = {}
        for currency in currencies:
            final_result[coin][currency] = str(fresh_data[coin][currency])

    return final_result