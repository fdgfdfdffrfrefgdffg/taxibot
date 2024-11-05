from aiogram import Router, F
from . import forwarder
from filters import IsClient

router = Router()
router.message.register(forwarder.get_client, IsClient())
router.message.register(forwarder.get_chat_id, F.text == "/id")

