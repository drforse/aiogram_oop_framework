from aiogram.types import Poll
from aiogram.dispatcher import FSMContext

from .base import BaseView


class PollView(BaseView):
    @classmethod
    async def execute(cls, p: Poll, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls):
        callback = cls.execute
        cls.dp.register_poll_handler(callback, *cls.custom_filters,
                                     run_task=cls.run_task, **cls.register_kwargs)
