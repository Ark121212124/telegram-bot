import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
import database  # создаёт таблицы при запуске

# handlers
from handlers import (
    start,
    news,
    contacts,
    subscribe,
    feedback,
    admin,
    chat_welcome
)


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # порядок важен
    dp.include_router(chat_welcome.router)  # приветствие в чатах
    dp.include_router(start.router)
    dp.include_router(news.router)
    dp.include_router(contacts.router)
    dp.include_router(subscribe.router)
    dp.include_router(feedback.router)
    dp.include_router(admin.router)

    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
