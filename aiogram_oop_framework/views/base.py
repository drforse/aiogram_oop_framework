from aiogram import Dispatcher, Bot


class BaseView:
    dp: Dispatcher = None
    bot: Bot = None

    custom_filters: list = None
    commands = None
    regexp = None
    content_types = None
    state = None
    run_task = None
    index = None
    register_kwargs: dict = None

    @classmethod
    def add_custom_filters(cls, *custom_filters):
        if not cls.custom_filters:
            cls.custom_filters = list()
        cls.custom_filters += custom_filters

    @classmethod
    def add_register_kwargs(cls, **kwargs):
        if not cls.register_kwargs:
            cls.register_kwargs = dict()
        cls.register_kwargs.update(kwargs)
