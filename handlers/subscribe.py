from aiogram import Router
from aiogram.types import Message
from database import cursor, conn

router = Router()

@router.message(lambda m: m.text == "🔔 Подписка")
async def sub(message: Message):
    try:
        cursor.execute("INSERT INTO subs VALUES(?)", (message.from_user.id,))
        conn.commit()
        await message.answer("Вы подписаны!")
    except:
        await message.answer("Вы уже подписаны.")