from aiogram.types import FSInputFile

@router.message(F.text == "/start")
async def start_cmd(message: Message):
    is_admin = message.from_user.id in ADMINS

    photo = FSInputFile("images/start.jpg")

    await message.answer_photo(
        photo=photo,
        caption="👋 Добро пожаловать!\n\nПосёлок Большая Елховка",
        reply_markup=user_kb(is_admin)
    )
