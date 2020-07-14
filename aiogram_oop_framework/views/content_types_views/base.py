from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from ..base import BaseView
from aiogram_oop_framework.exceptions import *


ALLOWED_UPDATE_TYPES = ['message', 'edited_message', 'channel_post', 'edited_channel_post']


class BaseContentTypesView(BaseView):
    content_types = None
    update_type = 'message'

    @classmethod
    async def execute(cls, m: Message, state: FSMContext = None, **kwargs):
        pass

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls.execute
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
        register_handler(callback, *custom_filters, regexp=cls.regexp,
                         content_types=cls.content_types, state=cls.state(), run_task=cls.run_task, **kwargs)

