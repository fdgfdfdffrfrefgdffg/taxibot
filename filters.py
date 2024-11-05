from aiogram.types import Message
from aiogram import Bot
from aiogram.filters import Filter
from config import private_groups, public_groups
from aiogram.enums import ChatMemberStatus
from sqldata import get_taxi
from config import inner_list

class CheckInDataBase(Filter):
    async def __call__(self, message: Message):
        return not bool(get_taxi(message.from_user.id))

class IsPrivateGroupUser(Filter):
    async def __call__(self, message: Message, bot: Bot):
        if message.chat.type == "private": return False
        for chat in private_groups:
            status = await bot.get_chat_member(chat_id=chat, user_id=message.from_user.id)
            if status.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]:
                return True
        else: 
            return False

class IsClient(Filter):
    async def __call__(self, message: Message, bot: Bot):
        if not message.text: return False 
        if message.chat.id in public_groups:
            user = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            if user.status in [ChatMemberStatus.MEMBER]:
                return True
    