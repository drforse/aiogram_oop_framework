from aiogram import Dispatcher
from aiogram.types import InlineQuery
from aiogram.dispatcher import FSMContext

from .base import BaseView


class InlineQueryView(BaseView):
    """View for updates of type "message"

    Attributes:
        custom_filters (list): Custom filters (for ex.: [lambda m: m.reply_to_message]).

        state (Callable): Function, which returns a State object of aiogram or "*"

        run_task (bool): Run callback in task (no wait results)

        register_kwargs (dict): Kwargs, which you would add in @dp.message_handler in fresh aiogram


    You may found more info about attributes in aiogram's docs on Dispatcher.message_handler or you may not, depends on aiogram's docs.

    """
    @classmethod
    async def execute(cls, q: InlineQuery, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    async def _execute(cls, q: InlineQuery, state: FSMContext = None, **kwargs):
        await cls.execute(q, state, **kwargs)

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_inline_handler(callback, *custom_filters, state=cls.state(),
                                   run_task=cls.run_task, **kwargs)
