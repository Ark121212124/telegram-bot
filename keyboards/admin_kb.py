from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить новость")],
        [KeyboardButton(text="🗂 Управление новостями")],
        [KeyboardButton(text="📢 Рассылка")],
        [KeyboardButton(text="⬅ В меню")]
    ],
    resize_keyboard=True
)
