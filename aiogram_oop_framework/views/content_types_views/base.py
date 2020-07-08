from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from ..base import BaseView
from aiogram_oop_framework.exceptions import *


ALLOWED_UPDATE_TYPES = ['message', 'edited_message', 'channel_post', 'edited_channel_post']


class BaseContentTypesView(BaseView):
    content_types = None
    __update_type = 'message'

    @property
    def update_type(self):
        return self.__update_type

    @update_type.setter
    def update_type(self, value: str):
        if value not in ALLOWED_UPDATE_TYPES:
            raise WrongUpdateType(f"update_type must be one of {ALLOWED_UPDATE_TYPES}")
        self.__update_type = value

    @classmethod
    async def execute(cls, m: Message, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls):
        callback = cls.execute
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
        register_handler(callback=callback, *cls.custom_filters, regexp=cls.regexp,
                         content_types=cls.content_types, state=cls.state, run_task=cls.run_task, **cls.register_kwargs)

