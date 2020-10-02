from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext

from aiogram_oop_framework.views import CommandView


class Start(CommandView):
    """start doc"""
    @classmethod
    async def execute(cls, m: Message, state: FSMContext = None, **kwargs):
        await m.answer('hi')
