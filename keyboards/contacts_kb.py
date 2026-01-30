from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contacts_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏛 Администрация поселения")],
        [KeyboardButton(text="🗂 МФЦ")],
        [KeyboardButton(text="🚰 МУП ЖКХ Елховское")],
        [KeyboardButton(text="🏢 УК Лямбирькомжилсервис")],
        [KeyboardButton(text="🏥 Большеелховская амбулатория")],
        [KeyboardButton(text="⬅ В меню")]
    ],
    resize_keyboard=True
)
