import logging

from aiogram import Dispatcher
from aiogram.types import Poll
from aiogram.dispatcher import FSMContext

from .base import BaseView
from ..filters import Filters


class PollView(BaseView):
    @classmethod
    async def execute(cls, p: Poll, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    async def _execute(cls, p: Poll, state: FSMContext = None, **kwargs):

        for _, method in cls.__dict__.items():
            if not isinstance(method, (classmethod, staticmethod)):
                continue
            func = method.__func__
            if not hasattr(func, "__execute_filters__"):
                continue

            filters: Filters = func.__execute_filters__
            if not filters:
                continue
            if await filters.poll_matches(p):
                if isinstance(method, classmethod):
                    await func(cls, p)
                else:
                    logging.warning("using staticmethods is deprecated in version 0.2.dev2, "
                                    "use only classmethods")
                    await func(p)
                return

        await cls.execute(p, state, **kwargs)

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_poll_handler(callback, *custom_filters,
                                 run_task=cls.run_task, **kwargs)
