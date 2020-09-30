import logging

from aiogram import Dispatcher
from aiogram.types import Poll
from aiogram.dispatcher import FSMContext

from .base import BaseView


class PollView(BaseView):
    @classmethod
    async def execute(cls, p: Poll, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_poll_handler(callback, *custom_filters,
                                 run_task=cls.run_task, **kwargs)
