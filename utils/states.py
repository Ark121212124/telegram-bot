from aiogram.fsm.state import State, StatesGroup

class AddNewsState(StatesGroup):
    title = State()
    text = State()
    photo = State()
    link = State()
