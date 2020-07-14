import typing

from aiogram import Bot


class BaseView:
    """
    Base class for all views
    all fields of BaseView including bot should remain unchanged
    """

    bot: Bot = None

    # aiogram register args
    custom_filters: list = None
    commands: list = None
    regexp: str = None
    content_types: list = None
    state: typing.Callable = lambda: None
    run_task = None
    register_kwargs: dict = None

    # aiogram_oop_framework settings
    index: int = None
    auto_register: bool = True

    @classmethod
    def add_custom_filters(cls, *custom_filters) -> None:
        if not cls.custom_filters:
            cls.custom_filters = list()
        cls.custom_filters += custom_filters

    @classmethod
    def add_register_kwargs(cls, **kwargs) -> None:
        if not cls.register_kwargs:
            cls.register_kwargs = dict()
        cls.register_kwargs.update(kwargs)
