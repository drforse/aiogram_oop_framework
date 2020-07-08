from aiogram.types import ContentType

from aiogram_oop_framework.views.message import MessageView
from aiogram_oop_framework.exceptions import *


ALLOWED_UPDATE_TYPES = ['message', 'edited_message', 'channel_post', 'edited_channel_post']


class CommandView(MessageView):
    __update_type = 'message'
    append_commands = True
    content_types = [ContentType.TEXT]

    @property
    def update_type(self):
        return self.__update_type

    @update_type.setter
    def update_type(self, value: str):
        if value not in ALLOWED_UPDATE_TYPES:
            raise WrongUpdateType(f"update_type must be one of {ALLOWED_UPDATE_TYPES}")
        self.__update_type = value

    @classmethod
    def register(cls):
        """

        :param append_commands: if commands is not None and append_commands is True, library appends default,
                                generated by class.__name__.lower() command to to commands' list
                                (if commands is None, this parameter is ignored,
                                 to make view without command, use Message insted)
        :return:
        """
        callback = cls.execute
        default_command = cls.__name__.lower()
        commands = cls.commands
        if not cls.commands:
            commands = [default_command]
        elif cls.append_commands:
            commands.append(default_command)

        if cls.__update_type == 'message':
            register_handler = cls.dp.register_message_handler
        elif cls.__update_type == 'edited_message':
            register_handler = cls.dp.register_edited_message_handler
        elif cls.__update_type == 'channel_post':
            register_handler = cls.dp.register_channel_post_handler
        elif cls.__update_type == 'edited_channel_post':
            register_handler = cls.dp.register_edited_channel_post_handler
        else:
            raise WrongUpdateType(f"update_type is {cls.__update_type}, but must be one of {ALLOWED_UPDATE_TYPES}")

        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []

        register_handler(callback=callback, *custom_filters, commands=commands, regexp=cls.regexp,
                         content_types=cls.content_types, state=cls.state, run_task=cls.run_task, **kwargs)
