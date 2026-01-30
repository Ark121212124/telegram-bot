import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import database

from handlers import start, news, subscribe, feedback, admin

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(news.router)
    dp.include_router(subscribe.router)
    dp.include_router(feedback.router)
    dp.include_router(admin.router)

    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
