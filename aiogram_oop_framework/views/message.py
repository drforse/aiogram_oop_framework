from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext

from .base import BaseView


class MessageView(BaseView):
    """View for updates of type "message"

    Attributes:
        custom_filters (list): Custom filters (for ex.: [lambda m: m.reply_to_message]).

        commands (list): List of commands (for ex.: ['start', 'help']).

        regexp (str): Regexp string for matching message text/caption (for ex.: r'^hello$')

        content_types (list): List of content_type's of message (for ex.: ['text', 'photo'])

        state (Callable): Function, which returns a State object of aiogram or "*"

        run_task (bool): Run callback in task (no wait results)

        register_kwargs (dict): Kwargs, which you would add in @dp.message_handler in fresh aiogram


    You may found more info about attributes in aiogram's docs on Dispatcher.message_handler or you may not, depends on aiogram's docs.

    """
    @classmethod
    async def execute(cls, m: types.Message, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls, dp: Dispatcher):
        """Make sure you don't want to use a more high-level view like CommandView or PhotoView instead"""
        callback = cls.execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_message_handler(callback, *custom_filters, commands=cls.commands,
                                    regexp=cls.regexp, content_types=cls.content_types, state=cls.state(),
                                    run_task=cls.run_task, **kwargs)

