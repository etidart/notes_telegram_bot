from aiogram import Router, types, F
from aiogram.filters.callback_data import CallbackData
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from utils.db.db import add_note_db

router = Router()

note_content = []

class Note(StatesGroup):
    title = State()
    content = State()

@router.callback_query(Text(text="create_note"))
async def create_note(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название", reply_markup=ReplyKeyboardRemove())
    await callback.answer()
    await state.set_state(Note.title)

@router.message(Note.title)
async def title_chosen(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Хорошо. Теперь содержание\nКогда закончите напишите 'закончить' или /end")
    await state.set_state(Note.content)

@router.message(Note.content, Command(commands=["end"]))
@router.message(Note.content, F.text.casefold() == "закончить")
async def content_end(message: Message, state: FSMContext):
    global note_content
    print("1")
    note_title = (await state.get_data())['title']
    print("2 " + note_title)
    add_note_db(message.from_user.id, note_title, note_content)
    await message.answer("Заметка сохранена\n/start - возврат к главному меню")
    note_content = []
    await state.clear()
    print("3")

@router.message(Note.content)
async def content_add(message: Message, state: FSMContext):
    global note_content
    note_content.append(message.text)
    print(note_content)

