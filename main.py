import asyncio
from price_fetcher import fetch_prices
import json

async def main():
    coins = ["bitcoin", "ethereum", "solana"]
    currencies = ["usd", "rub"]

    print("Запрашиваем курсы у CoinGecko...")
    prices = await fetch_prices(coins, currencies)
    
    print(json.dumps(prices, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(main())