from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📰 Новости")],
        [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="✉ Обратная связь")],
        [KeyboardButton(text="🔔 Подписка")]
    ],
    resize_keyboard=True
)
