from aiogram import Router, F
from aiogram.types import Message
from config import ADMINS
from keyboards.admin_kb import admin_kb
from keyboards.user_kb import user_kb

router = Router()

# вход через /admin
@router.message(F.text == "/admin")
async def admin_panel_cmd(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("Админ панель", reply_markup=admin_kb)

# вход через кнопку
@router.message(F.text == "🛠 Админ панель")
async def admin_panel_btn(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("Админ панель", reply_markup=admin_kb)

# выход
@router.message(F.text == "⬅ В меню")
async def back_to_menu(message: Message):
    await message.answer("Главное меню", reply_markup=user_kb(True))
