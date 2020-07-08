from aiogram.types import PollAnswer
from aiogram.dispatcher import FSMContext

from .base import BaseView


class PollAnswerView(BaseView):
    @classmethod
    async def execute(cls, p: PollAnswer, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls):
        callback = cls.execute
        cls.dp.register_poll_answer_handler(callback, *cls.custom_filters,
                                            run_task=cls.run_task, **cls.register_kwargs)
