from aiogram.types import InlineQuery
from aiogram.dispatcher import FSMContext

from .base import BaseView


class InlineQueryView(BaseView):
    @classmethod
    async def execute(cls, q: InlineQuery, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls):
        callback = cls.execute
        cls.dp.register_inline_handler(callback, *cls.custom_filters, state=cls.state,
                                       run_task=cls.run_task, **cls.register_kwargs)
