from aiogram import Dispatcher

from .message import MessageView


class EditedChannelPostView(MessageView):
    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_edited_channel_post_handler(callback, *custom_filters, commands=cls.commands,
                                                regexp=cls.regexp, content_types=cls.content_types, state=cls.state(),
                                                run_task=cls.run_task, **kwargs)
