from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from config import ADMINS
from keyboards.admin_kb import admin_kb
from keyboards.user_kb import user_kb
from utils.states import AddNewsState
from database import cursor, conn

router = Router()

# ===== ВХОД В АДМИНКУ =====

@router.message(F.text == "/admin")
async def admin_panel_cmd(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("Админ панель", reply_markup=admin_kb)

@router.message(F.text == "🛠 Админ панель")
async def admin_panel_btn(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("Админ панель", reply_markup=admin_kb)

@router.message(F.text == "⬅ В меню")
async def back_to_menu(message: Message):
    await message.answer("Главное меню", reply_markup=user_kb(True))


# ===== ДОБАВЛЕНИЕ НОВОСТИ =====

@router.message(F.text == "➕ Добавить новость")
async def add_news_start(message: Message, state: FSMContext):
    if message.from_user.id not in ADMINS:
        return

    await message.answer("Введите заголовок новости:")
    await state.set_state(AddNewsState.title)


@router.message(AddNewsState.title)
async def add_news_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Введите текст новости:")
    await state.set_state(AddNewsState.text)


@router.message(AddNewsState.text)
async def add_news_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Отправьте фото новости:")
    await state.set_state(AddNewsState.photo)


@router.message(AddNewsState.photo)
async def add_news_photo(message: Message, state: FSMContext):
    if not message.photo:
        await message.answer("Нужно отправить именно фото.")
        return

    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)

    await message.answer("Отправьте ссылку на новость:")
    await state.set_state(AddNewsState.link)


@router.message(AddNewsState.link)
async def add_news_link(message: Message, state: FSMContext):
    data = await state.get_data()

    title = data["title"]
    text = data["text"]
    photo = data["photo"]
    link = message.text

    cursor.execute(
        "INSERT INTO news(title, text, photo, link) VALUES(?,?,?,?)",
        (title, text, photo, link)
    )
    conn.commit()

    await message.answer("Новость успешно добавлена!", reply_markup=admin_kb)
    await state.clear()
