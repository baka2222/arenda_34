from bot import bot, dp
import asyncio
from handlers import (start_handler, apartaments_handler, prices_handler)


async def main():
    dp.include_router(start_handler.start_rt)
    dp.include_router(apartaments_handler.apartaments_rt)
    dp.include_router(prices_handler.prices_rt)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())