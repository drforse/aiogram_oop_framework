from aiogram import types
from aiogram.dispatcher import FSMContext

from .base import BaseView


class MessageView(BaseView):
    @classmethod
    async def execute(cls, m: types.Message, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls):
        """

        Make sure you don't want to use a more high-level like Command or Photo view instead
        """
        callback = cls.execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        cls.dp.register_message_handler(callback, *custom_filters, commands=cls.commands,
                                        regexp=cls.regexp, content_types=cls.content_types, state=cls.state,
                                        run_task=cls.run_task, **kwargs)

