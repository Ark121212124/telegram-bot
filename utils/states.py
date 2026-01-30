from aiogram.fsm.state import State, StatesGroup

class AddNews(StatesGroup):
    title = State()
    text = State()
    photo = State()
    link = State()

class Feedback(StatesGroup):
    name = State()
    phone = State()
    message = State()
    photo = State()
