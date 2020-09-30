import functools
from typing import Union, Callable, List, Dict, Optional, Awaitable

from aiogram import Dispatcher
from aiogram.types import *
from aiogram.types.base import TelegramObject
from aiogram.utils import helper
from aiogram.dispatcher.filters import check_filters, FilterNotPassed, get_filters_spec
from aiogram.dispatcher.handler import Handler, FilterObj

from aiogram_oop_framework.exceptions import WrappedFunctionWrongAnnotations, WrongUpdateType


class DiceEmojiHelper(helper.Helper):
    DICE = helper.Item('🎲')
    DART = helper.Item('🎯')
    BASKETBALL = helper.Item('🏀')


class UpdateType(helper.Helper):

    mode = helper.HelperMode.snake_case

    MESSAGE = helper.Item()  # message
    EDITED_MESSAGE = helper.Item()  # edited_message
    CHANNEL_POST = helper.Item()  # channel_post
    EDITED_CHANNEL_POST = helper.Item()  # edited_channel_post
    INLINE_QUERY = helper.Item()  # inline_query
    CHOSEN_INLINE_QUERY = helper.Item()  # chosen_inline_result
    CALLBACK_QUERY = helper.Item()  # callback_query
    SHIPPING_QUERY = helper.Item()  # shipping_query
    PRE_CHECKOUT_QUERY = helper.Item()  # pre_checkout_query
    POLL = helper.Item()  # poll
    POLL_ANSWER = helper.Item()  # poll_answer


async def tg_obj_matches_filters(tg_obj: TelegramObject, filters: List[FilterObj]):
    try:
        # print(filters)
        await check_filters(filters, [tg_obj])
    except FilterNotPassed:
        # print(tg_obj)
        # print(filters)
        return False
    return True


def filter_execute(*args, update_type: str = None, **filters):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        func_filters = wrapper.__execute_filters__ if hasattr(wrapper, "__execute_filters__") else []
        dp = Dispatcher.get_current()
        if update_type:
            handler = _get_handler_by_update_type_name(dp, update_type)
        else:
            handler = _get_handler_by_func(dp, func)
        if not handler and not update_type:
            raise WrappedFunctionWrongAnnotations(
                'filter_execute wrapped function must take one of telegram update types, which '
                'must be aiogram\'s TelegramObject as first parameter, and be properly annotated, '
                'in other case filter_execute\'s parameter update_type must not be None')
        if not handler:
            raise WrongUpdateType('update_type must be a valid telegram update type')
        content_types = filters.get('content_types') or ContentType.all()
        if handler.middleware_key == 'message':
            func_filters += get_filters_spec(
                dp, dp.filters_factory.resolve(handler, *args, content_types=content_types, **filters))
        else:
            func_filters += get_filters_spec(
                dp, dp.filters_factory.resolve(handler, *args, **filters))
        wrapper.__execute_filters__ = func_filters
        return wrapper
    return decorator


def elem_matches_filter(fltr, value) -> bool:
    if fltr is None:
        return False
    if isinstance(fltr, Callable):
        fltr = fltr()
    if isinstance(value, list):
        for f in fltr:
            if f in value:
                return True
        return False
    return value in fltr


def _get_handler_by_func(dp: Dispatcher, func: [Callable, Awaitable]) -> Optional[Handler]:
    hander_type: type = list(func.__annotations__.values())[0]
    handler_by_type_object = {
        Message: dp.message_handlers,
        InlineQuery: dp.inline_query_handlers,
        ChosenInlineResult: dp.chosen_inline_result_handlers,
        CallbackQuery: dp.callback_query_handlers,
        ShippingQuery: dp.shipping_query_handlers,
        PreCheckoutQuery: dp.pre_checkout_query_handlers,
        Poll: dp.poll_handlers,
        PollAnswer: dp.poll_answer_handlers}
    return handler_by_type_object.get(hander_type)


def _get_handler_by_update_type_name(dp: Dispatcher, update_type: str) -> Optional[Handler]:
    handler_by_type_name = {
        UpdateType.MESSAGE: dp.message_handlers,
        UpdateType.EDITED_MESSAGE: dp.edited_message_handlers,
        UpdateType.CHANNEL_POST: dp.channel_post_handlers,
        UpdateType.EDITED_CHANNEL_POST: dp.edited_channel_post_handlers,
        UpdateType.INLINE_QUERY: dp.inline_query_handlers,
        UpdateType.CHOSEN_INLINE_QUERY: dp.chosen_inline_result_handlers,
        UpdateType.CALLBACK_QUERY: dp.callback_query_handlers,
        UpdateType.SHIPPING_QUERY: dp.shipping_query_handlers,
        UpdateType.PRE_CHECKOUT_QUERY: dp.pre_checkout_query_handlers,
        UpdateType.POLL: dp.poll_handlers,
        UpdateType.POLL_ANSWER: dp.poll_answer_handlers}
    return handler_by_type_name.get(update_type)
