from aiogram.fsm.state import State, StatesGroup


class AddNewsState(StatesGroup):
    title = State()
    text = State()
    photo = State()
    link = State()


class FeedbackState(StatesGroup):
    name = State()
    phone = State()
    message = State()


class ManageNewsState(StatesGroup):
    choose_id = State()
    action = State()
    edit_field = State()
    new_value = State()
