from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# keyboard buttons
create_btn = InlineKeyboardButton(text="Создать заметку", callback_data="create_note")
find_btn = InlineKeyboardButton(text="Найти заметку", callback_data="find_note")
delete_btn = InlineKeyboardButton(text="Удалить заметку", callback_data="delete_note")

# keyboard
keyboard = InlineKeyboardMarkup(inline_keyboard=[[create_btn, find_btn, delete_btn]])