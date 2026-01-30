from aiogram import Router, F
from aiogram.types import Message
from database import cursor

router = Router()

@router.message(F.text == "📰 Новости")
async def news(message: Message):
    cursor.execute("SELECT * FROM news ORDER BY id DESC")
    rows = cursor.fetchall()

    if not rows:
        await message.answer("Новостей пока нет.")
        return

    for row in rows:
        _, title, text, photo, link = row
        await message.answer_photo(
            photo=photo,
            caption=f"<b>{title}</b>\n{text}\n{link}",
            parse_mode="HTML"
        )
