from aiogram import Dispatcher
from aiogram.types import PollAnswer
from aiogram.dispatcher import FSMContext

from .base import BaseView


class PollAnswerView(BaseView):
    @classmethod
    async def execute(cls, p: PollAnswer, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls.execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_poll_answer_handler(callback, *custom_filters,
                                        run_task=cls.run_task, **kwargs)
