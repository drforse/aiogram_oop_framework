import typing
import logging

from aiogram import Bot
from aiogram.types.base import TelegramObject
from aiogram.dispatcher import FSMContext

from ..filters.filters import tg_obj_matches_filters
from ..utils import class_is_original


class MetaBaseView(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if class_is_original(cls, 'aiogram_oop_framework'):
            return
        methods_with_filters = []
        for _, method in cls.__dict__.items():
            if not isinstance(method, (classmethod, staticmethod)):
                continue
            func = method.__func__
            if not hasattr(func, "__execute_filters__"):
                continue
            methods_with_filters.append(method)
        cls._methods_with_filters = methods_with_filters


class BaseView(metaclass=MetaBaseView):
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
    help_text: str = ""
    command_description: str = ""

    @classmethod
    def get_help(cls) -> str:
        return cls.help_text or cls.__doc__

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

    @classmethod
    async def execute(cls, tg_obj: TelegramObject, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    async def _execute(cls, tg_obj: TelegramObject, state: FSMContext = None, **kwargs):
        """
        this is a private method used by the framework for making filters like execute_in_private work

        :param tg_obj: Message, CallbackQuery, InlineQuery etc
        :param state: FSMContext
        :param kwargs: kwargs
        :return:
        """
        for method in cls._methods_with_filters:
            func = method.__func__
            filters = func.__execute_filters__
            if not filters:
                continue
            if await tg_obj_matches_filters(tg_obj, filters):
                if isinstance(method, classmethod):
                    await func(cls, tg_obj)
                else:
                    logging.warning("using staticmethods is deprecated in version 0.2.dev2, "
                                    "use only classmethods")
                    await func(tg_obj)
                return

        await cls.execute(tg_obj, state, **kwargs)
