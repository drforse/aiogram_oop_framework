from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram_oop_framework.views import MessageView


class Example(MessageView):

    @staticmethod
    async def execute(m: types.Message, state: FSMContext = None, **kwargs):
        """execute if chat type is not private, neither supergroup"""
        await m.answer('undef')

    @staticmethod
    async def execute_in_private(m: types.Message, state: FSMContext = None, **kwargs):
        """execute in private chat"""
        await m.answer('gg private brr')

    @classmethod
    async def execute_in_supergroup(cls, m: types.Message, state: FSMContext = None, **kwargs):
        """execute in supergroup chat"""
        if m.chat.id == 124565432:
            await cls.execute(m)
            return
        await m.answer('gg supergroup brr')

    @staticmethod
    async def execute_in_anus(m: types.Message, state: FSMContext = None, **kwargs):
        """it is never called as there is not chat type "anus"
        (but if telegram will create such a type, this will start working)"""
        await m.answer("Аааааа сука на сторону заднеприводных перекочевал?\n"
                       "Променял теплую дырку на длинный банан? В бублика долбиться решил?")
