from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="отмена")]],
        resize_keyboard=True
    )