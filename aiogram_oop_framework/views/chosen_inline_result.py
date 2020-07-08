from aiogram.types import ChosenInlineResult
from aiogram.dispatcher import FSMContext

from .base import BaseView


class ChosenInlineResultView(BaseView):
    @classmethod
    async def execute(cls, r: ChosenInlineResult, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls):
        callback = cls.execute
        cls.dp.register_chosen_inline_handler(callback, *cls.custom_filters, state=cls.state,
                                              run_task=cls.run_task, **cls.register_kwargs)
