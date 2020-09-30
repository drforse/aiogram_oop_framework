from aiogram import types
from aiogram.types.chat import ChatType
from aiogram.types.message_entity import MessageEntityType
from aiogram.types.poll import PollType
from aiogram.dispatcher import FSMContext

from aiogram_oop_framework.views import CallbackQueryView
from aiogram_oop_framework.filters.filters import filter_execute, DiceEmojiHelper


class TestCallbackQueryView(CallbackQueryView):
    @classmethod
    async def execute(cls, q: types.CallbackQuery, state: FSMContext = None, **kwargs):
        m = q.message
        assert m.chat.type != ChatType.SUPER_GROUP
        if m.poll:
            assert m.poll.type != PollType.QUIZ
        if m.dice:
            assert m.dice.emoji not in [DiceEmojiHelper.DART, DiceEmojiHelper.BASKETBALL]

        assert q.from_user.id != 123456789

    @classmethod
    @filter_execute(chat_type=ChatType.SUPER_GROUP)
    async def execute_for_supergroups(cls, q: types.CallbackQuery, state: FSMContext = None, **kwargs):
        assert q.message.chat.type == ChatType.SUPER_GROUP

    @classmethod
    @filter_execute(poll_type="quiz")
    async def execute_for_quizzes(cls, q: types.CallbackQuery, state: FSMContext = None, **kwargs):
        m = q.message
        assert m.chat.type != ChatType.SUPER_GROUP

        entities = m.entities or m.caption_entities
        entities = m.poll.explanation_entities if m.poll else entities
        entities_types = [e.type for e in entities]
        assert MessageEntityType.MENTION not in entities_types

        assert m.poll.type == PollType.QUIZ

    @classmethod
    @filter_execute(dice_emoji=["dart", DiceEmojiHelper.BASKETBALL])
    async def execute_for_dart_and_basket(cls, q: types.CallbackQuery, state: FSMContext = None, **kwargs):
        m = q.message
        assert m.chat.type != ChatType.SUPER_GROUP
        if m.poll:
            assert m.poll.type != PollType.QUIZ

        entities = m.entities or m.caption_entities
        entities = m.poll.explanation_entities if m.poll else entities
        entities_types = [e.type for e in entities]
        assert MessageEntityType.MENTION not in entities_types

        assert m.dice is not None
        assert m.dice.emoji in [DiceEmojiHelper.DART, DiceEmojiHelper.BASKETBALL]

    @classmethod
    @filter_execute(func=lambda q: q.from_user.id == 123456789)
    async def execute_for_user(cls, q: types.CallbackQuery, state: FSMContext = None, **kwargs):
        m = q.message
        assert m.chat.type != ChatType.SUPER_GROUP
        if m.poll:
            assert m.poll.type != PollType.QUIZ
        if m.dice:
            assert m.dice.emoji not in [DiceEmojiHelper.DART, DiceEmojiHelper.BASKETBALL]

        entities = m.entities or m.caption_entities
        entities = m.poll.explanation_entities if m.poll else entities
        entities_types = [e.type for e in entities]
        assert MessageEntityType.MENTION not in entities_types

        assert q.from_user.id == 123456789
