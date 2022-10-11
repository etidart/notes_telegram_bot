from email import message
from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import row_generator
from utils.db.db import get_all_notes, get_note_content

router = Router()

class NoteViewer(StatesGroup):
    choosen_id = State()

notes = None

@router.callback_query(Text(text="show_note"))
async def show_note_start(callback: types.CallbackQuery, state: FSMContext):
    global notes
    notes = get_all_notes(callback.from_user.id)
    for number in range(len(notes)):
        await callback.message.answer(str(number + 1) + ". " + str(notes[number][1]), reply_markup=ReplyKeyboardRemove())
    callback.message.answer("Напишите номер заметки, которую хотите прочитать", reply_markup=ReplyKeyboardRemove())
    await state.set_state(NoteViewer.choosen_id)
    await callback.answer()

@router.message(NoteViewer.choosen_id)
async def show_content(message: Message, state: FSMContext):
    global notes
    content = get_note_content(notes[int(message.text)-1][0])
    for item in content:
        await message.answer(str(item), reply_markup=ReplyKeyboardRemove())
    await message.answer("Конец\n/start - возврат к главному меню", reply_markup=ReplyKeyboardRemove())
    notes = None
    await state.clear()
