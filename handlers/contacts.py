from aiogram import Router, F
from aiogram.types import Message

from keyboards.contacts_kb import contacts_kb
from keyboards.user_kb import user_kb
from config import ADMINS

router = Router()


# ===== ОТКРЫТИЕ МЕНЮ КОНТАКТОВ =====

@router.message(F.text == "📞 Контакты")
async def show_contacts(message: Message):
    await message.answer(
        "📞 Контакты организаций\n\nВыберите организацию:",
        reply_markup=contacts_kb
    )


# ===== ДАННЫЕ ОРГАНИЗАЦИЙ =====

contacts_data = {
    "🏛 Администрация поселения": (
        "🏛 Администрация поселения\n\n"
        "📍 с. Большая Елховка, ул. Фабричная, 21\n"
        "🕘 Пн–Пт: 08:30–17:30\n"
        "Перерыв: 13:00–14:00\n"
        "Сб–Вс: выходной"
    ),
    "🗂 МФЦ": (
        "🗂 МФЦ\n\n"
        "📍 ул. Фабричная, 21\n"
        "🕘 Пн–Пт: 08:30–17:00\n"
        "Сб–Вс: выходной"
    ),
    "🚰 МУП ЖКХ Елховское": (
        "🚰 МУП ЖКХ Елховское\n\n"
        "📍 с. Лямбирь, ул. Полевая, 17\n"
        "🕘 Пн–Пт: 08:00–17:00\n"
        "Перерыв: 12:00–13:00"
    ),
    "🏢 УК Лямбирькомжилсервис": (
        "🏢 УК Лямбирькомжилсервис\n\n"
        "📍 ул. Заводская, 1\n"
        "🕘 Пн–Пт: 07:45–16:30\n"
        "Перерыв: 12:00–13:00"
    ),
    "🏥 Большеелховская амбулатория": (
        "🏥 Большеелховская амбулатория\n\n"
        "📍 ул. Имерякова, 33\n"
        "🕘 Пн–Пт: 09:00–18:00"
    ),
}


# ===== ОБРАБОТКА ВЫБОРА ОРГАНИЗАЦИИ =====

@router.message(F.text.in_(contacts_data.keys()))
async def send_contact_info(message: Message):
    await message.answer(contacts_data[message.text])


# ===== ВОЗВРАТ В ГЛАВНОЕ МЕНЮ =====

@router.message(F.text == "⬅ В меню")
async def back_to_main(message: Message):
    is_admin = message.from_user.id in ADMINS
    await message.answer("Главное меню", reply_markup=user_kb(is_admin))
