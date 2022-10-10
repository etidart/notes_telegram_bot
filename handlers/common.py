from aiogram import Router
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards import main_kb

router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.answer(text="Этот бот необходим для создания заметок из нескольких сообщений\nИспользуйте кнопки ниже для взаимодействия", reply_markup=main_kb.keyboard)