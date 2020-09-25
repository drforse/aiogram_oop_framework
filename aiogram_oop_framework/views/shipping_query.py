from aiogram import Dispatcher
from aiogram.types import ShippingQuery
from aiogram.dispatcher import FSMContext

from .base import BaseView


class ShippingQueryView(BaseView):
    @classmethod
    async def execute(cls, q: ShippingQuery, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    async def _execute(cls, q: ShippingQuery, state: FSMContext = None, **kwargs):
        await cls.execute(q, state, **kwargs)

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_shipping_query_handler(callback, *custom_filters, state=cls.state(),
                                           run_task=cls.run_task, **kwargs)
