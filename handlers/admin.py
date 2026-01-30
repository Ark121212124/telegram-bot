from aiogram import Router
from aiogram.types import Message
from config import ADMINS
from keyboards.admin_kb import admin_kb

router = Router()

@router.message(lambda m: m.from_user.id in ADMINS)
async def admin_panel(message: Message):
    if message.text == "/admin":
        await message.answer("Админ панель", reply_markup=admin_kb)
