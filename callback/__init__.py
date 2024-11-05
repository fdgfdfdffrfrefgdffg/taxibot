from aiogram import Router, F
from . import acc

router = Router()
router.callback_query.register(acc.acc_order_call, F.data.startswith("acc"))