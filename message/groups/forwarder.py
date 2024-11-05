from aiogram import Bot
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import inner_list, private_groups
from aiogram.enums.parse_mode import ParseMode

async def get_chat_id(message: Message):
    await message.answer(f"Chat id: {message.chat.id}")

async def get_client(message: Message, bot: Bot):    
    flag = True
    for group in private_groups:
        msg = await message.forward(chat_id=group)
        if msg.forward_from:
            pass
        else: 
            flag = False
            await msg.delete()
            break
    
    if flag: await message.delete()
    if flag:
        await bot.send_message(
        message.chat.id,
        f"🙂 Hurmatli mijoz Sizni buyurtangiz koʻrib ciqilmoqda 🚕")
        await message.answer("🚗🚕🚙")
    
