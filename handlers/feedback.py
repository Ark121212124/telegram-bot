from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import FeedbackState
from config import ADMINS

router = Router()

@router.message(F.text == "✉ Обратная связь")
async def feedback_start(message: Message, state: FSMContext):
    await message.answer("Введите ФИО:")
    await state.set_state(FeedbackState.name)

@router.message(FeedbackState.name)
async def fb_phone(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Телефон:")
    await state.set_state(FeedbackState.phone)

@router.message(FeedbackState.phone)
async def fb_text(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Сообщение:")
    await state.set_state(FeedbackState.message)

@router.message(FeedbackState.message)
async def fb_done(message: Message, state: FSMContext):
    data = await state.get_data()

    text = f"Обращение:\n{data['name']}\n{data['phone']}\n{message.text}"

    for admin in ADMINS:
        await message.bot.send_message(admin, text)

    await message.answer("Сообщение отправлено!")
    await state.clear()
