from aiogram.fsm.state import State, StatesGroup


# ===== ДОБАВЛЕНИЕ НОВОСТИ =====
class AddNewsState(StatesGroup):
    title = State()
    text = State()
    photo = State()
    link = State()


# ===== ОБРАТНАЯ СВЯЗЬ =====
class FeedbackState(StatesGroup):
    name = State()
    phone = State()
    message = State()
    photo = State()   # необязательное фото


# ===== УПРАВЛЕНИЕ НОВОСТЯМИ =====
class ManageNewsState(StatesGroup):
    choose_id = State()
    action = State()
    edit_field = State()
    new_value = State()
