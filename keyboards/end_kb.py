from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = [[KeyboardButton(text="закончить"), KeyboardButton(text="отмена")]]

keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )