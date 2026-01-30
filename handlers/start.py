from aiogram import Router, F
from aiogram.types import Message
from keyboards.user_kb import user_kb
from config import ADMINS

router = Router()

@router.message(F.text == "/start")
async def start_cmd(message: Message):
    is_admin = message.from_user.id in ADMINS

    await message.answer_photo(
        photo="https://via.placeholder.com/600x300.png",
        caption="👋 Добро пожаловать!",
        reply_markup=user_kb(is_admin)
    )
