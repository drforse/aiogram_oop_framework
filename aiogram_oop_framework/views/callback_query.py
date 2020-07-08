from aiogram.types import InlineQuery
from aiogram.dispatcher import FSMContext

from .base import BaseView


class CallbackQueryView(BaseView):
    @classmethod
    async def execute(cls, q: InlineQuery, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls):
        callback = cls.execute
        cls.dp.register_callback_query_handler(callback, *cls.custom_filters, state=cls.state,
                                               run_task=cls.run_task, **cls.register_kwargs)
