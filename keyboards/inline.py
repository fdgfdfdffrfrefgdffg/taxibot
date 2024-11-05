from aiogram.utils.keyboard import InlineKeyboardBuilder

def acc_order_button(chat_id, full_name):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Qabul qilish", callback_data=f"acc:{full_name}:{chat_id}")
    return builder.as_markup()

