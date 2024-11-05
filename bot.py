from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import message, callback
from sqldata import close_db
import logging
from asyncio import run
dp = Dispatcher()






async def main():
    bot = Bot(BOT_TOKEN)
    logging.basicConfig(level=logging.INFO)
    dp.include_router(message.router)
    dp.include_router(callback.router)
    await dp.start_polling(bot)
    close_db()
run(main())