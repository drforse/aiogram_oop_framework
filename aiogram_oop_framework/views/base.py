import typing
import logging

from aiogram import Bot
from aiogram.types.base import TelegramObject
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import _check_spec, _get_spec

from ..filters.filters import tg_obj_matches_filters
from ..utils import class_is_original


class MetaBaseView(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if class_is_original(cls, 'aiogram_oop_framework'):
            return
        methods_with_filters = []
        pre_middlwares = []
        post_middlwares = []

        def append_methods_with_filters(cls_):
            for _, method in cls_.__dict__.items():
                if not isinstance(method, (classmethod, staticmethod)):
                    continue
                func = method.__func__
                if hasattr(func, "__execute_filters__"):
                    methods_with_filters.append(method)
                elif func.__name__.startswith("pre_"):
                    pre_middlwares.append(method)
                elif func.__name__.startswith("post_"):
                    post_middlwares.append(method)

        for base in cls.__bases__:
            if class_is_original(base, 'aiogram_oop_framework'):
                continue
            append_methods_with_filters(base)
        append_methods_with_filters(cls)
        cls._methods_with_filters = methods_with_filters
        cls._pre_middlwares = pre_middlwares
        cls._post_middlwares = post_middlwares

        # backward compatibility
        if cls.short_description:
            cls.command_description = cls.short_description
        elif cls.command_description:
            cls.short_description = cls.command_description
        # backward compatibility


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
    command_description: str = ""  # backward compatibility
    short_description: str = ""
    set_my_commands = 'first'  # None, 'first', 'all', [command, command]

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
        this is a private method used by the framework for making filters and middlwares work

        :param tg_obj: Message, CallbackQuery, InlineQuery etc
        :param state: FSMContext
        :param kwargs: kwargs
        :return:
        """

        executed = False
        try:
            for method in cls._pre_middlwares:
                func = method.__func__
                partial_data = cls.get_partial_data(func, state=state, **kwargs)
                await func(cls, tg_obj, **partial_data)

            for method in cls._methods_with_filters:
                func = method.__func__
                filters = func.__execute_filters__
                if not filters:
                    continue
                if await tg_obj_matches_filters(tg_obj, filters):
                    partial_data = cls.get_partial_data(func, state=state, **kwargs)
                    if isinstance(method, classmethod):
                        await func(cls, tg_obj, **partial_data)
                    else:
                        logging.warning("using staticmethods is deprecated in version 0.2.dev2, "
                                        "use only classmethods")
                        await func(tg_obj, **partial_data)
                    executed = True
                    break

            if not executed:
                partial_data = cls.get_partial_data(cls.execute, state=state, **kwargs)
                await cls.execute(tg_obj, **partial_data)
        finally:
            for method in cls._post_middlwares:
                func = method.__func__
                partial_data = cls.get_partial_data(func, state=state, **kwargs)
                await func(cls, tg_obj, **partial_data)

    @classmethod
    def get_partial_data(cls, func, **data):
        spec = _get_spec(func)
        return _check_spec(spec, data)
