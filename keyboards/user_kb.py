from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def user_kb(is_admin=False):
    kb = [
        [KeyboardButton(text="📰 Новости")],
        [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="✉ Обратная связь")],
        [KeyboardButton(text="🔔 Подписка")]
    ]

    if is_admin:
        kb.append([KeyboardButton(text="🛠 Админ панель")])

    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
