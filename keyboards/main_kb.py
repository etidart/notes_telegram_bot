from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# keyboard buttons
create_btn = InlineKeyboardButton(text="Создать заметку", callback_data="create_note")
show_btn = InlineKeyboardButton(text="Просмотреть заметку", callback_data="show_note")
delete_btn = InlineKeyboardButton(text="Удалить заметку", callback_data="delete_note")

# keyboard
keyboard = InlineKeyboardMarkup(inline_keyboard=[[create_btn], [show_btn], [delete_btn]])