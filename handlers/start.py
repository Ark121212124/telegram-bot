from aiogram import Router, F
from aiogram.types import Message
from keyboards.user_kb import main_kb

router = Router()

@router.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer_photo(
        photo="https://via.placeholder.com/600x300.png",
        caption="👋 Добро пожаловать!\nВыберите раздел ниже:",
        reply_markup=main_kb
    )
