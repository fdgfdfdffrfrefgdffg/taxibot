from aiogram import Bot
from aiogram.types import CallbackQuery
from sqldata import get_taxi
from aiogram.enums.parse_mode import ParseMode

async def acc_order_call(call: CallbackQuery, bot: Bot):
    full_name = call.data.split(":")[1]
    chat_id = call.data.split(":")[2]
    print(chat_id)
    taxi = get_taxi(call.from_user.id)
    if taxi:
        await bot.send_message(
            chat_id,
            f"""
🚕 {full_name} sizni buyurtmangiz qabul qilindi!

Taksis ma'lumotlari:
Ism: {taxi[1]}
Telefon raqam: XX XXX {taxi[2][-4:]}
""", parse_mode=ParseMode.MARKDOWN
        )
        await call.message.answer(f"{call.message.md_text}\n\n✅ Qabul qilindi!", parse_mode=ParseMode.MARKDOWN)
        await call.message.delete()
    else:
        await call.answer("Siz avval botdan ro'yhatdan o'ting!", show_alert=True)