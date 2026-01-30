from aiogram import Router, F
from aiogram.types import Message
from config import ADMINS
from keyboards.admin_kb import admin_kb

router = Router()

@router.message(F.text == "/admin")
async def admin_panel(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("Админ панель", reply_markup=admin_kb)
