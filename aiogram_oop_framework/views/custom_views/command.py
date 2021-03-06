from aiogram import Dispatcher
from aiogram.types import ContentType

from aiogram_oop_framework.utils import CommandCaseHelper
from aiogram_oop_framework.views.message import MessageView
from aiogram_oop_framework.exceptions import *


ALLOWED_UPDATE_TYPES = ['message', 'edited_message', 'channel_post', 'edited_channel_post']


class CommandView(MessageView):
    """May be same as :class:`aiogram_oop_framework.views.message.MessageView`, or
    :class:`aiogram_oop_framework.views.edited_message_view.EditedMessageView`, or
    :class:`aiogram_oop_framework.views.channel_post_view.ChannelPostView`, or
    :class:`aiogram_oop_framework.views.edited_channel_post_view.EditedChannelPostView`,
    dependently on update_type field, with difference that content_types field defaults to [ContentType.TEXT],
    and it has some differences, look down:

    Attributes:
        commands (list): commands list (not necessary, default command is auto-generated basing on class's name)
        update_type (str): Update type, must be one of: 'message', 'edited_message', 'channel_post', 'edited_channel_post', defaults to 'message'
        append_commands (bool): if True -> appends default auto-generated command to commands; ignored (just uses default auto-generated command) if bool(commands) is False
        default_command_case (str): default auto-generated command's case (snake_case/lowercase)

    while registering looks at your view's name and creates a default command with it (Start -> ['start'])

    """
    update_type = 'message'
    append_commands = True
    default_command_case = CommandCaseHelper.snake_case
    content_types = [ContentType.TEXT]

    @classmethod
    def register(cls, dp: Dispatcher):
        """
        """
        callback = cls._execute
        default_command = CommandCaseHelper.apply(cls.__name__, cls.default_command_case)
        commands = cls.commands
        if not cls.commands:
            commands = [default_command]
        elif cls.append_commands:
            commands.append(default_command)
        cls.commands = commands

        if cls.update_type == 'message':
            register_handler = dp.register_message_handler
        elif cls.update_type == 'edited_message':
            register_handler = dp.register_edited_message_handler
        elif cls.update_type == 'channel_post':
            register_handler = dp.register_channel_post_handler
        elif cls.update_type == 'edited_channel_post':
            register_handler = dp.register_edited_channel_post_handler
        else:
            raise WrongUpdateType(f"update_type is {cls.update_type}, but must be one of {ALLOWED_UPDATE_TYPES}")

        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []

        register_handler(callback, *custom_filters, commands=commands, regexp=cls.regexp,
                         content_types=cls.content_types, state=cls.state(), run_task=cls.run_task, **kwargs)
