from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext

from aiogram_oop_framework.utils import get_help
from aiogram_oop_framework.views import CommandView
from aiogram_oop_framework.filters.filters import filter_execute


class Help(CommandView):
    """your description for you and other developers"""
    help_text = "help help for users"

    @classmethod
    async def execute(cls, m: Message, state: FSMContext = None, **kwargs):
        await m.answer('...\n\nWrite /help &lt;command&gt; for more info')

    @classmethod
    @filter_execute(lambda m: m.get_args(), update_type='message')
    async def execute_with_args(cls, m: Message, state: FSMContext = None, **kwargs):
        help_ = get_help(m.get_args())
        if help_:
            await m.answer(help_)
        else:
            await m.answer("Sry, help for command isn't found")
