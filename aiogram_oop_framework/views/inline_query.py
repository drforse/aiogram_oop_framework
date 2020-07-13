from aiogram import Dispatcher
from aiogram.types import InlineQuery
from aiogram.dispatcher import FSMContext

from .base import BaseView


class InlineQueryView(BaseView):
    @classmethod
    async def execute(cls, q: InlineQuery, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls.execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_inline_handler(callback, *custom_filters, state=cls.state,
                                   run_task=cls.run_task, **kwargs)
