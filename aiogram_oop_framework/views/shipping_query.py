from aiogram.types import ShippingQuery
from aiogram.dispatcher import FSMContext

from .base import BaseView


class ShippingQueryView(BaseView):
    @classmethod
    async def execute(cls, q: ShippingQuery, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls):
        callback = cls.execute
        cls.dp.register_shipping_query_handler(callback, *cls.custom_filters, state=cls.state,
                                               run_task=cls.run_task, **cls.register_kwargs)
