from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить новость")],
        [KeyboardButton(text="⚙ Управление новостями")]
    ],
    resize_keyboard=True
)