import functools
from typing import Union, Callable, List, Dict, Optional

from aiogram.types import Message, CallbackQuery, Poll
from aiogram.types.base import TelegramObject
from aiogram.utils import helper

from .exceptions import FilterNameImpossible


FILTER_ANNOTATION = Union[str, helper.Item, List[helper.Item]]
FILTER_ANNOTATION = Union[FILTER_ANNOTATION, List[FILTER_ANNOTATION]]
FILTER_ANNOTATION = Optional[Union[FILTER_ANNOTATION, Callable[[TelegramObject], FILTER_ANNOTATION]]]


class DiceEmojiHelper(helper.Helper):
    DICE = helper.Item('🎲')
    DART = helper.Item('🎯')
    BASKETBALL = helper.Item('🏀')


class Filters:

    def __init__(self):
        self.chat_member_status: FILTER_ANNOTATION = None
        self.chat_type: FILTER_ANNOTATION = None
        self.contains_entities_types: FILTER_ANNOTATION = None
        self.poll_type: FILTER_ANNOTATION = None
        self.dice_emoji: FILTER_ANNOTATION = None
        self.func: Callable = lambda x: True

    async def _validate_for_message(self, m: Message):
        if self.poll_type and not m.poll:
            return False
        if self.dice_emoji and not m.dice:
            return False
        return True

    async def _validate_for_callback_query(self, q: CallbackQuery):
        if self.poll_type and not q.message.poll:
            return False
        if self.dice_emoji and not q.message.dice:
            return False
        return True

    async def message_matches(self, m: Message):
        if await self._validate_for_message(m) is False:
            return False
        if self.chat_type and not elem_matches_filter(self.chat_type, m.chat.type):
            return False
        if self.chat_member_status:
            member = await m.bot.get_chat_member(m.chat.id, m.from_user.id)
            if not elem_matches_filter(self.chat_member_status, member.status):
                return False
        if self.contains_entities_types:
            entities = m.entities or m.caption_entities
            entities = m.poll.explanation_entities if m.poll else entities
            entities_types = [e.type for e in entities]
            if not elem_matches_filter(self.contains_entities_types, entities_types):
                return False
        if self.poll_type and not elem_matches_filter(self.poll_type, m.poll.type):
            return False
        if self.dice_emoji and not elem_matches_filter(self.dice_emoji, m.dice.emoji):
            return False
        if self.func:
            return self.func(m)
        return True

    async def callback_query_matches(self, q: CallbackQuery):
        if await self._validate_for_callback_query(q) is False:
            return False
        if self.chat_type and not elem_matches_filter(self.chat_type, q.message.chat.type):
            return False
        if self.chat_member_status:
            member = await q.bot.get_chat_member(q.message.chat.id, q.from_user.id)
            if not elem_matches_filter(self.chat_member_status, member.status):
                return False
        if self.contains_entities_types:
            entities = q.message.entities or q.message.caption_entities
            entities = q.message.poll.explanation_entities if q.message.poll else entities
            entities_types = [e.type for e in entities]
            if not elem_matches_filter(self.contains_entities_types, entities_types):
                return False
        if self.poll_type and not elem_matches_filter(self.poll_type, q.message.poll.type):
            return False
        if self.dice_emoji and not elem_matches_filter(self.dice_emoji, q.message.dice.emoji):
            return False
        if self.func:
            return self.func(q)
        return True

    async def poll_matches(self, p: Poll):
        if self.contains_entities_types and not elem_matches_filter(self.contains_entities_types, p.explanation_entities):
            return False
        if self.poll_type and not elem_matches_filter(self.poll_type, p.type):
            return False
        if self.func:
            return self.func(p)
        return True

    def __str__(self):
        return (f"<Filters(chat_member_status={self.chat_member_status}, "
                f"chat_type={self.chat_type}, contains_entities={self.contains_entities_types}, "
                f"poll_type={self.poll_type}, dice_emoji={self.dice_emoji}, "
                f"func={self.func})>")


def filter_execute(**filters: Dict[str, FILTER_ANNOTATION]):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        func_filters: Filters = wrapper.__execute_filters__ if hasattr(wrapper, "__execute_filters__") else Filters()
        for fltr_type, fltr_value in filters.items():
            if not hasattr(func_filters, fltr_type):
                raise FilterNameImpossible(f"Not possible filter: {fltr_type}, "
                                           f"see all possible filters in filters.Filters or in docs")
            setattr(func_filters, fltr_type, fltr_value)
        wrapper.__execute_filters__ = func_filters
        return wrapper
    return decorator


def elem_matches_filter(fltr: FILTER_ANNOTATION, value) -> bool:
    if fltr is None:
        return False
    if isinstance(fltr, Callable):
        fltr = fltr()
    value_is_list = isinstance(value, list)
    fltr_is_list = isinstance(fltr, list)
    if value_is_list and fltr_is_list:
        for v in value:
            if v in fltr:
                return True
        return False
    if value_is_list:
        return fltr in value
    if fltr_is_list:
        return value in fltr
    return value == fltr
