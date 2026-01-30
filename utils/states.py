from aiogram.fsm.state import State, StatesGroup


# ===== ДОБАВЛЕНИЕ НОВОСТЕЙ =====
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
