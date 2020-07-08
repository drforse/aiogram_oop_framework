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
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        cls.dp.register_callback_query_handler(callback, *custom_filters, state=cls.state,
                                               run_task=cls.run_task, **kwargs)
