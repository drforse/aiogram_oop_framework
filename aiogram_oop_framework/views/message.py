import logging

from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext

from .base import BaseView
from ..filters import Filters, elem_matches_filter, filter_execute


class MessageView(BaseView):
    """View for updates of type "message"

    Attributes:
        custom_filters (list): Custom filters (for ex.: [lambda m: m.reply_to_message]).

        commands (list): List of commands (for ex.: ['start', 'help']), defaults to None

        regexp (str): Regexp string for matching message text/caption (for ex.: r'^hello$'), defaults to None

        content_types (list): List of content_type's of message (for ex.: ['text', 'photo']), defaults to None

        state (Callable): Function, which returns a State object of aiogram or "*", defaults to lambda: None

        run_task (bool): Run callback in task (no wait results), defaults to None

        register_kwargs (dict): Kwargs, which you would add in @dp.message_handler in fresh aiogram, defaults to None

        index (int): in which order to register the view, defaults to None

        auto_register (bool): set to False if you don't want re register the view autcomatically, ignored, if AUTO_REGISTER_VIEWS in settings.py is set to False, defaults to True


    Make sure you don't want to use a more high-level view like :class:`aiogram_oop_framework.views.custom_views.command.CommandView` or :class:`aiogram_oop_framework.views.content_types_views.text.TextView` instead.

    You may found more info about custom_filters, commands, regexp, content_types, state and run_task attributes attributes in aiogram's docs on Dispatcher.message_handler or you may not, depends on aiogram's docs.

    """

    @classmethod
    async def execute(cls, m: types.Message, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    async def _execute(cls, m: types.Message, state: FSMContext = None, **kwargs):

        # remove with execute_in_<chat_type> removing
        chat_type = m.chat.type
        if hasattr(cls, f'execute_in_{chat_type}'):
            logging.warning("execute_in_<chat_type> is deprecated in version 0.2.dev0, "
                            "use decorator filters.filter_execute() instead: "
                            "`filters.filter_execute(chat_type=<chat_type>)`")
            in_chat_method = cls.__dict__[f'execute_in_{chat_type}']
            func = in_chat_method.__func__
            if hasattr(func, "__execute_filters__"):
                fltrs = func.__execute_filters__
            else:
                fltrs = Filters()
            if fltrs.chat_type is None:
                fltrs.chat_type = chat_type
                func.__execute_filters__ = fltrs
        # remove with execute_in_<chat_type> removing

        for method in cls._methods_with_filters:
            func = method.__func__
            filters: Filters = func.__execute_filters__
            if not filters:
                continue
            if await filters.message_matches(m):
                if isinstance(method, classmethod):
                    await func(cls, m)
                else:
                    logging.warning("using staticmethods is deprecated in version 0.2.dev2, "
                                    "use only classmethods")
                    await func(m)
                return

        await cls.execute(m, state, **kwargs)

    @classmethod
    def register(cls, dp: Dispatcher):
        """method to register the handler, normally called automatically in manage.initialize_project()

        Parameters:
            dp (Dispatcher): in which dispatcher to register the handler

        """
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_message_handler(callback, *custom_filters, commands=cls.commands,
                                    regexp=cls.regexp, content_types=cls.content_types, state=cls.state(),
                                    run_task=cls.run_task, **kwargs)

