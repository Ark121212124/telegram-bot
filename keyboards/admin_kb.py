from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# главная админ клавиатура
admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить новость")],
        [KeyboardButton(text="🗂 Управление новостями")],
        [KeyboardButton(text="⬅ В меню")]
    ],
    resize_keyboard=True
)

# клавиатура действий с новостью
manage_news_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✏ Редактировать")],
        [KeyboardButton(text="🗑 Удалить")],
        [KeyboardButton(text="⬅ В меню")]
    ],
    resize_keyboard=True
)

# клавиатура редактирования полей
edit_fields_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Заголовок")],
        [KeyboardButton(text="Текст")],
        [KeyboardButton(text="Фото")],
        [KeyboardButton(text="Ссылка")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)
