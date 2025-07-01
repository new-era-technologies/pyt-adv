import asyncio
import logging
import sys
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from utils.handlers import router


load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")


async def main() -> None:
    bot = Bot(token=TOKEN)
    dp = Dispatcher()   
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())