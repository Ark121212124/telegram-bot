from aiogram.types import FSInputFile

@router.message(F.text == "/start")
async def start_cmd(message: Message):
    is_admin = message.from_user.id in ADMINS

    photo = FSInputFile("images/start.png")

    await message.answer_photo(
        photo=photo,
caption=(
    "Добро пожаловать!\n\n"
    "Информационный бот посёлка Большая Елховка.\n"
    "Актуальные новости, контакты учреждений "
    "и приём обращений граждан."
)

