from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import AddTaxiState
from sqldata import add_taxi


async def sign_up(message: Message, state: FSMContext):
    await message.answer("Ism-familyangizni kiriting.")
    await state.set_state(AddTaxiState.name)

async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Yaxshi, endi telefon raqamingizni yuboring.")
    await state.set_state(AddTaxiState.phone)

async def get_phone(message: Message, state: FSMContext):
    context = await state.get_data()
    add_taxi(
        message.from_user.id,
        context.get("name"),
        message.text
    )
    await message.answer("✅")
    await state.clear()