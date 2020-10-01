from aiogram.dispatcher.filters.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

from .filters import elem_matches_filter


class Entities(BoundFilter):
    """
    Check if message.entities/message.caption_entities/poll.explanation_entities contains entities of specified types
    """

    key = "entities"

    def __init__(self, entities):
        self.entities_types = entities if isinstance(entities, (list, set, tuple)) else [entities]

    async def check(self, tg_type) -> bool:
        if isinstance(tg_type, Message):
            if tg_type.poll:
                entities = [e.type for e in tg_type.poll.explanation_entities]
            else:
                entities = [e.type for e in tg_type.entities]
        else:
            entities = [e.type for e in tg_type.explanation_entities]
        return elem_matches_filter(self.entities_types, entities)


class ChatTypeFilter(BoundFilter):
    """
    check if chat.type is one of specified
    """

    key = "chat_type"

    def __init__(self, chat_type):
        self.chat_type = chat_type if isinstance(chat_type, (list, set, tuple)) else [chat_type]

    async def check(self, tg_type) -> bool:
        if isinstance(tg_type, Message):
            return elem_matches_filter(self.chat_type, tg_type.chat.type)
        else:
            return elem_matches_filter(self.chat_type, tg_type.message.chat.type)


class ChatMemberStatus(BoundFilter):
    """
    check if user's status in the chat is one of the specified
    """

    key = "chat_member_status"

    def __init__(self, chat_member_status):
        self.chat_member_status = chat_member_status if isinstance(chat_member_status, (list, set, tuple)) else [chat_member_status]

    async def check(self, tg_type) -> bool:
        if isinstance(tg_type, Message):
            member = await tg_type.bot.get_chat_member(tg_type.chat.id, tg_type.from_user.id)
        else:
            member = await tg_type.bot.get_chat_member(tg_type.message.chat.id, tg_type.from_user.id)
        return elem_matches_filter(self.chat_member_status, member.status)


class PollTypeFilter(BoundFilter):
    """
    check if poll's type is one of the specified
    """

    key = "poll_type"

    def __init__(self, poll_type):
        self.poll_type = poll_type if isinstance(poll_type, (list, set, tuple)) else [poll_type]

    async def check(self, tg_type) -> bool:
        if isinstance(tg_type, Message):
            if tg_type.poll is None:
                return False
            return elem_matches_filter(self.poll_type, tg_type.poll.type)
        elif isinstance(tg_type, CallbackQuery):
            if tg_type.message.poll is None:
                return False
            return elem_matches_filter(self.poll_type, tg_type.message.poll.type)
        else:
            return elem_matches_filter(self.poll_type, tg_type.type)


class DiceEmoji(BoundFilter):
    """
    check if dice's emoji is one of the specified
    """

    key = "dice_emoji"

    def __init__(self, dice_emoji):
        self.dice_emoji = dice_emoji if isinstance(dice_emoji, (list, set, tuple)) else [dice_emoji]

    async def check(self, tg_type) -> bool:
        if isinstance(tg_type, Message):
            if tg_type.dice is None:
                return False
            return elem_matches_filter(self.dice_emoji, tg_type.dice.emoji)
        else:
            if tg_type.message.dice is None:
                return False
            return elem_matches_filter(self.dice_emoji, tg_type.message.dice.emoji)


class FuncFilter(BoundFilter):
    """
        DEPRECATED IN VERSION 0.2.dev4

    executes function with passing TelegramObject's subclass' instance
    as parameter and checks if the result is True or False
    needed for backward compatibility, you can simply write your func for *args (ex.: `filter_execute(func)`)
    """

    key = "func"

    def __init__(self, func):
        self.func = func

    async def check(self, tg_type) -> bool:
        return self.func(tg_type)


__all__ = ["Entities",
           "ChatTypeFilter",
           "ChatMemberStatus",
           "PollTypeFilter",
           "DiceEmoji",
           "FuncFilter"]
