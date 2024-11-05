from aiogram.fsm.state import State, StatesGroup

class AddTaxiState(StatesGroup):
    name = State()
    phone = State()