from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import Feedback
from config import ADMINS

router = Router()

@router.message(lambda m: m.text == "✉ Обратная связь")
async def fb_start(message: Message, state: FSMContext):
    await message.answer("Введите ФИО:")
    await state.set_state(Feedback.name)

@router.message(Feedback.name)
async def fb_phone(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Телефон:")
    await state.set_state(Feedback.phone)

@router.message(Feedback.phone)
async def fb_msg(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Сообщение:")
    await state.set_state(Feedback.message)

@router.message(Feedback.message)
async def fb_done(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f"Обращение:\n{data['name']}\n{data['phone']}\n{message.text}"

    for admin in ADMINS:
        await message.bot.send_message(admin, text)

    await message.answer("Отправлено!")
    await state.clear()
