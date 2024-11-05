from aiogram import Router
from aiogram.filters import and_f
from filters import IsPrivateGroupUser, CheckInDataBase
from . import add_taxi
from states import AddTaxiState

router = Router()
# router.message.register(add_taxi.get_name, AddTaxiState.name)
# router.message.register(add_taxi.get_phone, AddTaxiState.phone)
# router.message.register(add_taxi.sign_up, and_f(IsPrivateGroupUser(), CheckInDataBase()))
