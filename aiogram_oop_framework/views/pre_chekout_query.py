from aiogram import Dispatcher
from aiogram.types import PreCheckoutQuery
from aiogram.dispatcher import FSMContext

from .base import BaseView


class PreCheckoutQueryView(BaseView):

    @classmethod
    async def execute(cls, q: PreCheckoutQuery, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_pre_checkout_query_handler(callback, *custom_filters, state=cls.state(),
                                               run_task=cls.run_task, **kwargs)
