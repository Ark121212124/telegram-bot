from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import ADMINS
from keyboards.admin_kb import admin_kb, manage_news_kb, edit_fields_kb
from keyboards.user_kb import user_kb
from utils.states import AddNewsState, ManageNewsState
from database import cursor, conn

router = Router()

# ================= ВХОД В АДМИНКУ =================

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
    is_admin = message.from_user.id in ADMINS
    await message.answer("Главное меню", reply_markup=user_kb(is_admin))


# ================= ДОБАВЛЕНИЕ НОВОСТИ =================

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
        await message.answer("Пожалуйста отправьте фото.")
        return

    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)

    await message.answer("Отправьте ссылку на новость:")
    await state.set_state(AddNewsState.link)


@router.message(AddNewsState.link)
async def add_news_link(message: Message, state: FSMContext):
    data = await state.get_data()

    cursor.execute(
        "INSERT INTO news(title, text, photo, link) VALUES(?,?,?,?)",
        (data["title"], data["text"], data["photo"], message.text)
    )
    conn.commit()

    await message.answer("Новость добавлена!", reply_markup=admin_kb)
    await state.clear()


# ================= УПРАВЛЕНИЕ НОВОСТЯМИ =================

@router.message(F.text == "🗂 Управление новостями")
async def manage_news(message: Message, state: FSMContext):
    if message.from_user.id not in ADMINS:
        return

    cursor.execute("SELECT id, title FROM news ORDER BY id DESC")
    rows = cursor.fetchall()

    if not rows:
        await message.answer("Новостей нет.")
        return

    text = "Введите номер новости:\n\n"
    for row in rows:
        text += f"{row[0]}. {row[1]}\n"

    await message.answer(text)
    await state.set_state(ManageNewsState.choose_id)


@router.message(ManageNewsState.choose_id)
async def choose_news(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите номер цифрами.")
        return

    news_id = int(message.text)

    cursor.execute("SELECT id FROM news WHERE id=?", (news_id,))
    if not cursor.fetchone():
        await message.answer("Новость не найдена.")
        return

    await state.update_data(news_id=news_id)
    await message.answer("Выберите действие:", reply_markup=manage_news_kb)
    await state.set_state(ManageNewsState.action)


# ---------- УДАЛЕНИЕ ----------

@router.message(ManageNewsState.action, F.text == "🗑 Удалить")
async def delete_news(message: Message, state: FSMContext):
    data = await state.get_data()

    cursor.execute("DELETE FROM news WHERE id=?", (data["news_id"],))
    conn.commit()

    await message.answer("Новость удалена.", reply_markup=admin_kb)
    await state.clear()


# ---------- РЕДАКТИРОВАНИЕ ----------

@router.message(ManageNewsState.action, F.text == "✏ Редактировать")
async def edit_news(message: Message, state: FSMContext):
    await message.answer("Что изменить?", reply_markup=edit_fields_kb)
    await state.set_state(ManageNewsState.edit_field)


@router.message(ManageNewsState.edit_field)
async def choose_field(message: Message, state: FSMContext):
    field_map = {
        "Заголовок": "title",
        "Текст": "text",
        "Фото": "photo",
        "Ссылка": "link"
    }

    if message.text == "⬅ Назад":
        await message.answer("Админ панель", reply_markup=admin_kb)
        await state.clear()
        return

    if message.text not in field_map:
        await message.answer("Выберите кнопку.")
        return

    await state.update_data(field=field_map[message.text])

    if message.text == "Фото":
        await message.answer("Отправьте новое фото:")
    else:
        await message.answer("Введите новое значение:")

    await state.set_state(ManageNewsState.new_value)


@router.message(ManageNewsState.new_value)
async def update_value(message: Message, state: FSMContext):
    data = await state.get_data()
    news_id = data["news_id"]
    field = data["field"]

    if field == "photo":
        if not message.photo:
            await message.answer("Нужно отправить фото.")
            return
        value = message.photo[-1].file_id
    else:
        value = message.text

    cursor.execute(f"UPDATE news SET {field}=? WHERE id=?", (value, news_id))
    conn.commit()

    await message.answer("Новость обновлена!", reply_markup=admin_kb)
    await state.clear()
