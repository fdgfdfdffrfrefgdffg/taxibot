from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession
from config import BOT_TOKEN, active
from aiogram.filters import and_f
import message, callback
from sqldata import close_db
from filters import IsAdmin, IsSleep
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware
import logging

from asyncio import run
dp = Dispatcher()





# Faollik holatini boshqarish uchun holat
class BlockUpdatesMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.is_active = True

    async def __call__(self, handler, event, data):
        # Agar yangilanishlar bloklangan bo'lsa, faqat /on va /off buyruqlari o‘tishi kerak
        if not self.is_active and not (isinstance(event, Message) and event.text in ["/on", "/off"]):
            return  # Yangilanishlarni bloklash

        return await handler(event, data)

    async def toggle_updates(self, state: bool):
        self.is_active = state


# Middlewareni ro‘yxatga olish
block_middleware = BlockUpdatesMiddleware()
dp.message.middleware(block_middleware)

# /off buyrug'i uchun handler
@dp.message(and_f(Command(commands=["off"]), IsAdmin()))
async def off_command(message: Message):
    await block_middleware.toggle_updates(False)
    await message.answer("Bot yangilanishlarni qabul qilishni to'xtatdi.")

# /on buyrug'i uchun handler
@dp.message(and_f(Command(commands=["on"]), IsAdmin()))
async def on_command(message: Message):
    await block_middleware.toggle_updates(True)
    await message.answer("Bot yangilanishlarni qayta qabul qilishni boshladi.")


async def main():
    session = AiohttpSession(proxy="http://proxy.server:3128/")
    bot = Bot(BOT_TOKEN, session=session)
    # bot = Bot(BOT_TOKEN)
    logging.basicConfig(level=logging.INFO)

    dp.include_router(message.router)
    dp.include_router(callback.router)
    await dp.start_polling(bot)
    close_db()
run(main())