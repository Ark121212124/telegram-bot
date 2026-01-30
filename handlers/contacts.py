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
        "<b>🏛 Администрация поселения (с. Большая Елховка)</b>\n\n"
        "Орган местного самоуправления. Вопросы благоустройства, ЖКХ, "
        "социальной поддержки и муниципальных услуг жителям.\n\n"
        "📞 +7 (83441) 3-09-90\n"
        "📞 +7 (83441) 3-09-91"
    ),

    "🗂 МФЦ": (
        "<b>🗂 МФЦ Лямбирского района</b>\n\n"
        "Оформление документов и справок по принципу «одного окна»: "
        "паспорта, недвижимость, соцуслуги и гос-сервисы.\n\n"
        "📞 +7 (83441) 3-00-00"
    ),

    "🚰 МУП ЖКХ Елховское": (
        "<b>🚰 МУП «ЖКХ Елховское»</b>\n\n"
        "Коммунальное обслуживание поселения: водоснабжение, сети, "
        "вывоз отходов и благоустройство территорий.\n\n"
        "📞 +7 (83441) 3-10-16"
    ),

    "🏢 УК Лямбирькомжилсервис": (
        "<b>🏢 УК «Лямбирькомжилсервис»</b>\n\n"
        "Управление многоквартирными домами, ремонт и обслуживание "
        "общего имущества, работа с обращениями жителей.\n\n"
        "📞 +7 (83441) 3-10-07"
    ),

    "🏥 Большеелховская амбулатория": (
        "<b>🏥 Большеелховская амбулатория</b>\n\n"
        "Амбулаторная медицинская помощь населению: приём врачей, "
        "профосмотры, вакцинация и диагностика.\n\n"
        "📞 +7 (83441) 3-07-41"
    ),
}


# ===== ВЫБОР ОРГАНИЗАЦИИ =====

@router.message(F.text.in_(contacts_data.keys()))
async def send_contact_info(message: Message):
    await message.answer(
        contacts_data[message.text],
        parse_mode="HTML"
    )


# ===== ВОЗВРАТ В МЕНЮ =====

@router.message(F.text == "⬅ В меню")
async def back_to_main(message: Message):
    is_admin = message.from_user.id in ADMINS
    await message.answer("Главное меню", reply_markup=user_kb(is_admin))
