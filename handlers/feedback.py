from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.states import FeedbackState
from config import ADMINS

router = Router()


# ===== СТАРТ ОБРАТНОЙ СВЯЗИ =====

@router.message(F.text == "✉ Обратная связь")
async def feedback_start(message: Message, state: FSMContext):
    await message.answer("Введите ФИО:")
    await state.set_state(FeedbackState.name)


@router.message(FeedbackState.name)
async def fb_phone(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите телефон:")
    await state.set_state(FeedbackState.phone)


@router.message(FeedbackState.phone)
async def fb_text(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Опишите проблему:")
    await state.set_state(FeedbackState.message)


@router.message(FeedbackState.message)
async def fb_photo_request(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer(
        "Прикрепите фото (по желанию) или напишите 'нет':"
    )
    await state.set_state(FeedbackState.photo)


# ===== ПОЛУЧЕНИЕ ФОТО ИЛИ НЕТ =====

@router.message(FeedbackState.photo)
async def fb_finish(message: Message, state: FSMContext):
    data = await state.get_data()

    name = data["name"]
    phone = data["phone"]
    text = data["text"]

    caption = (
        f"📩 Новое обращение\n\n"
        f"👤 {name}\n"
        f"📞 {phone}\n\n"
        f"📝 {text}"
    )

    # если фото есть
    if message.photo:
        photo_id = message.photo[-1].file_id

        for admin in ADMINS:
            await message.bot.send_photo(
                admin,
                photo=photo_id,
                caption=caption
            )

    # если нет фото
    else:
        for admin in ADMINS:
            await message.bot.send_message(admin, caption)

    await message.answer("Обращение отправлено!")
    await state.clear()
