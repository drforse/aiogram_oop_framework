import pytest
from aiogram.types import Message

from aiogram_oop_framework.views import MessageView
from .types_dataset import MESSAGE


class ExecutionLogs:
    execution_logs = ""


class Start(MessageView):

    @classmethod
    async def pre_execute(cls, m, state=None, **kwargs):
        ExecutionLogs.execution_logs += "pre_execution"

    @classmethod
    async def pre_execute_1(cls, m, state=None, **kwargs):
        ExecutionLogs.execution_logs += "pre_execution_1"

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        ExecutionLogs.execution_logs += "execution"

    @classmethod
    async def post_execute(cls, m, state=None, **kwargs):
        ExecutionLogs.execution_logs += "post_execution"

    @classmethod
    async def post_execute_1(cls, m, state=None, **kwargs):
        ExecutionLogs.execution_logs += "post_execution_1"


@pytest.mark.asyncio
async def test_middlwares():
    await Start._execute(Message(**MESSAGE))
    assert ExecutionLogs.execution_logs == "pre_executionpre_execution_1executionpost_executionpost_execution_1"
