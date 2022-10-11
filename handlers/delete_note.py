from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from utils.db.db import get_all_notes, delete_note_db

router = Router()

class NoteDeleter(StatesGroup):
    choosen_id = State()

notes = None

@router.callback_query(Text(text="delete_note"))
async def delete_note_start(callback: types.CallbackQuery, state: FSMContext):
    global notes
    notes = get_all_notes(callback.from_user.id)
    for number in range(len(notes)):
        await callback.message.answer(str(number + 1) + ". " + str(notes[number][1]), reply_markup=ReplyKeyboardRemove())
    callback.message.answer("Напишите номер заметки, которую хотите удалить", reply_markup=ReplyKeyboardRemove())
    await state.set_state(NoteDeleter.choosen_id)
    await callback.answer()

@router.message(NoteDeleter.choosen_id)
async def delete_note(message: Message, state: FSMContext):
    global notes
    delete_note_db(notes[int(message.text)-1][0])
    await message.answer("Заметка удалена\n/start - возврат к главному меню", reply_markup=ReplyKeyboardRemove())
    notes = None
    await state.clear()