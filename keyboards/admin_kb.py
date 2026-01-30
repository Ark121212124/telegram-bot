from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить новость")],
        [KeyboardButton(text="📢 Рассылка")]
    ],
    resize_keyboard=True
)
