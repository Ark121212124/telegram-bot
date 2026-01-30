from aiogram import Router
from aiogram.types import Message
from keyboards.user_kb import main_kb

router = Router()

@router.message()
async def start(message: Message):
    if message.text == "/start":
        await message.answer_photo(
            photo="https://via.placeholder.com/600x300.png",
            caption="👋 Добро пожаловать!\nЗдесь вы найдете актуальные новости и информацию.",
            reply_markup=main_kb
        )