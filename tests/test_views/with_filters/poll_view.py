from aiogram import types
from aiogram.types.message_entity import MessageEntityType
from aiogram.types.poll import PollType
from aiogram.dispatcher import FSMContext

from aiogram_oop_framework.views import PollView
from aiogram_oop_framework.filters.filters import filter_execute


class TestPollView(PollView):
    @classmethod
    async def execute(cls, p: types.Poll, state: FSMContext = None, **kwargs):
        assert p.type != PollType.QUIZ

        assert p.explanation_entities is not None
        entities_types = [e.type for e in p.explanation_entities]
        assert MessageEntityType.MENTION not in entities_types

    @classmethod
    @filter_execute(entities=MessageEntityType.MENTION)
    async def execute_for_mentions(cls, p: types.Poll, state: FSMContext = None, **kwargs):
        assert p.explanation_entities is not None
        entities_types = [e.type for e in p.explanation_entities]
        assert MessageEntityType.MENTION in entities_types

    @classmethod
    @filter_execute(poll_type="quiz")
    async def execute_for_quizzes(cls, p: types.Poll, state: FSMContext = None, **kwargs):
        assert p.explanation_entities is not None
        entities_types = [e.type for e in p.explanation_entities]
        assert MessageEntityType.MENTION not in entities_types

        assert p.type == PollType.QUIZ

    @classmethod
    @filter_execute(func=lambda p: p.type == PollType.REGULAR)
    async def execute_for_regular_polls(cls, p: types.Poll, state: FSMContext = None, **kwargs):
        assert p.type != PollType.QUIZ

        assert p.explanation_entities is not None
        entities_types = [e.type for e in p.explanation_entities]
        assert MessageEntityType.MENTION not in entities_types

        assert p.type == "regular"
