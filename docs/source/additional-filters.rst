Additional Filters
===================


Different code execution dependently on chat type
-------------------------------------------------
You can add special methods to your views to execute different code dependently on chat type by writing execute_in_<chat_type>:

.. code-block:: python

    from aiogram import types
    from aiogram.dispatcher import FSMContext

    from aiogram_oop_framework.views import MessageView


    class Example(MessageView):

        @classmethod
        async def execute(cls, m: types.Message, state: FSMContext = None, **kwargs):
            """this will be executed if chat type is not private"""
            await m.answer('undef')

        @classmethod
        async def execute_in_private(cls, m: types.Message, state: FSMContext = None, **kwargs):
            """execute in private chat"""
            await m.answer('gg private brr')


Surely, it only works in views for objects, which may give access to chat like MessageView and CallbackQueryView, but NOT InlineQueryView
