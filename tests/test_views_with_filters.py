import pytest
from aiogram.types import Message, CallbackQuery, Poll

from .test_views.with_filters import TestMessageView, TestCallbackQueryView, TestPollView
from .types_dataset import *


@pytest.mark.asyncio
async def test_message_view():
    for message in [MESSAGE, MESSAGE_IN_SUPERGROUP,
                    MESSAGE_WITH_ENTITIES, MESSAGE_WITH_QUIZ,
                    MESSAGE_WITH_DICE, MESSAGE_FROM_123456789]:
        msg = Message(**message)
        await TestMessageView._execute(msg)


@pytest.mark.asyncio
async def test_callback_query_view():
    for query in [CALLBACK_QUERY, CALLBACK_QUERY_IN_SUPERGROUP,
                  CALLBACK_QUERY_WITH_MESSAGE_WITH_ENTITIES,
                  CALLBACK_QUERY_WITH_QUIZ_MESSAGE,
                  CALLBACK_QUERY_WITH_DICE_MESSAGE,
                  CALLBACK_QUERY_FROM_123456789]:
        q = CallbackQuery(**query)
        await TestCallbackQueryView._execute(q)


@pytest.mark.asyncio
async def test_poll_view():
    for poll in [QUIZ, QUIZ_WITH_ENTITIES, REGULAR_POLL]:
        p = Poll(**poll)
        await TestPollView._execute(p)
