from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.chat import ChatType
from aiogram_oop_framework.views import MessageView
from aiogram_oop_framework.filters import filter_execute


class Example(MessageView):

    @classmethod
    async def execute(cls, m: types.Message, state: FSMContext = None, **kwargs):
        """execute if chat type is not private, neither supergroup"""
        await m.answer('undef')

    @classmethod
    @filter_execute(chat_type=ChatType.PRIVATE)
    async def execute_in_private(cls, m: types.Message, state: FSMContext = None, **kwargs):
        """execute in private chat"""
        await m.answer('gg private brr')

    @classmethod
    @filter_execute(chat_type="supergroup")
    async def execute_in_supergroup(cls, m: types.Message, state: FSMContext = None, **kwargs):
        """execute in supergroup chat"""
        if m.chat.id == 124565432:
            await cls.execute(m)
            return
        await m.answer('gg supergroup brr')

    @classmethod
    @filter_execute(chat_type="anus")
    async def execute_in_anus(cls, m: types.Message, state: FSMContext = None, **kwargs):
        """it is never called as there is not chat type "anus"
        (but if telegram will create such a type, this will start working)"""
        await m.answer("Аааааа сука на сторону заднеприводных перекочевал?\n"
                       "Променял теплую дырку на длинный банан? В бублика долбиться решил?")
