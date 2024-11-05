from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from config import BOT_TOKEN
import message, callback
from sqldata import close_db

import logging
from asyncio import run
dp = Dispatcher()






async def main():
    
    session = AiohttpSession(proxy="http://proxy.server:3128/")
    bot = Bot(BOT_TOKEN, session=session)

    logging.basicConfig(level=logging.INFO)
    dp.include_router(message.router)
    dp.include_router(callback.router)
    await dp.start_polling(bot)
    close_db()
run(main())