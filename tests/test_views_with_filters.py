import pytest
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import *
from aiogram_oop_framework.filters.builtin import *
from .types_dataset import *

test_bot = Bot("123456:ABCDEfghi8385t5gfl4")
test_dp = Dispatcher(test_bot, storage=MemoryStorage())
Dispatcher.set_current(test_dp)

test_dp.filters_factory.bind(Entities, event_handlers=[test_dp.message_handlers, test_dp.poll_handlers])
test_dp.filters_factory.bind(ChatTypeFilter, event_handlers=[test_dp.message_handlers, test_dp.callback_query_handlers])
test_dp.filters_factory.bind(ChatMemberStatus, event_handlers=[test_dp.message_handlers, test_dp.callback_query_handlers])
test_dp.filters_factory.bind(PollTypeFilter,
                        event_handlers=[test_dp.message_handlers, test_dp.callback_query_handlers, test_dp.poll_handlers])
test_dp.filters_factory.bind(DiceEmoji, event_handlers=[test_dp.message_handlers, test_dp.callback_query_handlers])
test_dp.filters_factory.bind(FuncFilter)

from .test_views.with_filters import TestMessageView, TestCallbackQueryView, TestPollView


@pytest.mark.asyncio
async def test_message_view():
    for message in [MESSAGE, MESSAGE_IN_SUPERGROUP,
                    MESSAGE_WITH_ENTITIES, MESSAGE_WITH_QUIZ,
                    MESSAGE_WITH_DICE, MESSAGE_FROM_123456789]:
        msg = Message(**message)
        User.set_current(msg.from_user)
        Chat.set_current(msg.chat)
        await TestMessageView._execute(msg)


@pytest.mark.asyncio
async def test_callback_query_view():
    for query in [CALLBACK_QUERY, CALLBACK_QUERY_IN_SUPERGROUP,
                  CALLBACK_QUERY_WITH_MESSAGE_WITH_ENTITIES,
                  CALLBACK_QUERY_WITH_QUIZ_MESSAGE,
                  CALLBACK_QUERY_WITH_DICE_MESSAGE,
                  CALLBACK_QUERY_FROM_123456789]:
        q = CallbackQuery(**query)
        User.set_current(q.from_user)
        Chat.set_current(q.message.chat)
        await TestCallbackQueryView._execute(q)


@pytest.mark.asyncio
async def test_poll_view():
    for poll in [QUIZ, QUIZ_WITH_ENTITIES, REGULAR_POLL]:
        p = Poll(**poll)
        await TestPollView._execute(p)
