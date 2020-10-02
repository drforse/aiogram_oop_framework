from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from aiogram import Dispatcher

dp = Dispatcher.get_current()


@dp.message_handler(commands=['cancel'])
async def foo(m: Message, state: FSMContext = None, **kwargs):
    """cancel doc"""
    await m.answer('canceled')
