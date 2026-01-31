from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.new_chat_members)
async def bot_added_to_chat(message: Message):
    # проверяем, что добавили именно бота
    for member in message.new_chat_members:
        if member.id == message.bot.id:
            await message.answer(
                "🤖 БуП-Бип, привет, дорогие односельчане!\n\n"
                "Я — ваш дружелюбный *Бот Большеелховского поселения*, "
                "интерактивный помощник, созданный для того, чтобы сделать "
                "вашу жизнь чуть проще и веселее! 🎉\n\n"
                "Я здесь, чтобы помочь вам с кучей полезных функций, которые "
                "облегчают общение с органами местного самоуправления и "
                "местными организациями.\n\n"
                "Если вдруг я что-то не так пойму или закосячу — "
                "сообщите моему мудрому создателю: @Kre0s1 😉",
                parse_mode="Markdown"
            )
