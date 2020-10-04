import logging

from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext

from .base import BaseView


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

        auto_register (bool): set to False if you don't want register the view automatically, ignored, if AUTO_REGISTER_VIEWS in settings.py is set to False, defaults to True

        help_text (str): help's text to return by :ref:`aiogram_oop_framework.utils.get_help`, also user in utils.Commands to get description for command if command_description is empty or None

        command_description (str): command's description for every command in commands attribute to call set_my_commands in initialize_projects, if no view has command_desciption, then it is not called, also user in utils.Commands to get description for command


    Make sure you don't want to use a more high-level view like :class:`aiogram_oop_framework.views.custom_views.command.CommandView` or :class:`aiogram_oop_framework.views.content_types_views.text.TextView` instead.

    You may found more info about custom_filters, commands, regexp, content_types, state and run_task attributes attributes in aiogram's docs on Dispatcher.message_handler or you may not, depends on aiogram's docs.

    """

    @classmethod
    async def execute(cls, m: types.Message, state: FSMContext = None, **kwargs):
        raise NotImplementedError

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

