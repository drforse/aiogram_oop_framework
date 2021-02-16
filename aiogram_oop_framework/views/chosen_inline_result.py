from aiogram.types import ChosenInlineResult
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.types.base import TelegramObject

from .base import BaseView


class ChosenInlineResultView(BaseView):

    @classmethod
    async def execute(cls, r: ChosenInlineResult, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_chosen_inline_handler(callback, *custom_filters, state=cls.state(),
                                          run_task=cls.run_task, **kwargs)
