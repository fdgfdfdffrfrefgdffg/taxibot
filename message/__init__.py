from aiogram import Router
from . import groups, private

router = Router()
router.include_router(groups.router)
router.include_router(private.router)
