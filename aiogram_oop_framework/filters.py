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
        self.contains_entities: FILTER_ANNOTATION = None
        self.poll_type: FILTER_ANNOTATION = None
        self.dice_emoji: FILTER_ANNOTATION = None
        self.func: Callable = lambda x: True

    async def message_matches(self, m: Message):
        if self.chat_type and not elem_matches_filter(self.chat_type, m.chat.type):
            return False
        if self.chat_member_status:
            member = await m.bot.get_chat_member(m.chat.id, m.from_user.id)
            if not elem_matches_filter(self.chat_member_status, member.status):
                return False
        if self.contains_entities:
            entities = m.entities if m.text else m.caption_entities
            if not elem_matches_filter(self.contains_entities, entities):
                return False
        if self.poll_type and not elem_matches_filter(self.poll_type, m.poll.type):
            return False
        if self.dice_emoji and not elem_matches_filter(self.dice_emoji, m.dice.emoji):
            return False
        if self.func:
            return self.func(m)
        return True

    async def callback_query_matches(self, q: CallbackQuery):
        if self.chat_type and not elem_matches_filter(self.chat_type, q.message.chat.type):
            return False
        if self.chat_member_status:
            member = await q.bot.get_chat_member(q.message.chat.id, q.from_user.id)
            if not elem_matches_filter(self.chat_member_status, member.status):
                return False
        if self.contains_entities:
            entities = q.message.entities if q.message.text else q.message.caption_entities
            if not elem_matches_filter(self.contains_entities, entities):
                return False
        if self.poll_type and not elem_matches_filter(self.poll_type, q.message.poll.type):
            return False
        if self.dice_emoji and not elem_matches_filter(self.dice_emoji, q.message.dice.emoji):
            return False
        if self.func:
            return self.func(q)
        return True

    async def poll_matches(self, p: Poll):
        if self.contains_entities and not elem_matches_filter(self.contains_entities, p.explanation_entities):
            return False
        if self.poll_type and not elem_matches_filter(self.poll_type, p.type):
            return False
        if self.func:
            return self.func(p)
        return True


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
    if isinstance(fltr, list):
        return value in fltr
    return value == fltr
