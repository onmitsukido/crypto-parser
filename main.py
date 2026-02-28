import asyncio
import json
from core import get_prices_with_cache

async def main():
    coins = ["bitcoin", "ethereum", "solana"]
    currencies = ["usd", "rub"]

    print("Получаем курсы (с использованием кэша)...")
    prices = await get_prices_with_cache(coins, currencies)
    
    print(json.dumps(prices, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(main())