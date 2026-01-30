from aiogram import Router, F
from aiogram.types import Message
from database import cursor, conn

router = Router()

@router.message(F.text == "🔔 Подписка")
async def subscribe(message: Message):
    try:
        cursor.execute("INSERT INTO subs VALUES(?)", (message.from_user.id,))
        conn.commit()
        await message.answer("Вы подписаны на новости!")
    except:
        await message.answer("Вы уже подписаны.")
