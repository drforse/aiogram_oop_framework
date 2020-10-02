from aiogram import Dispatcher, Bot

from aiogram_oop_framework.views import CommandView, MessageView
from aiogram_oop_framework.utils import get_help


bot = Bot("34342323:sdfvcawfeedfr")
dp = Dispatcher(bot)


class CView(CommandView):
    """start help"""
    commands = ['start']
    help_text = "overrited start help"

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        return


class C1View(CommandView):
    """help help"""
    update_type = 'edited_message'
    commands = ['help']

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        return


class MView(MessageView):
    """cancel help"""
    commands = ['cancel']

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        return


class M1View(MessageView):
    """cancel1 help"""
    commands = ['cancel']

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        return


CView.register(dp)
C1View.register(dp)
MView.register(dp)
M1View.register(dp)


class JustClass:

    @classmethod
    async def foo(cls, m):
        """go1 help"""
        return


dp.register_message_handler(JustClass.foo, commands=['go1'])


@dp.message_handler(commands=['go'])
async def foo(m):
    """go help"""
    return


def test_get_start_help():
    Dispatcher.set_current(dp)
    assert get_help('start') == "overrited start help"


def test_get_help_help():
    Dispatcher.set_current(dp)
    assert get_help('help') == "help help"


def test_get_cancel_help():
    Dispatcher.set_current(dp)
    assert get_help('cancel') == "cancel help"


def test_get_go_help():
    Dispatcher.set_current(dp)
    assert get_help('go') == "go help"


def test_get_go1_help():
    Dispatcher.set_current(dp)
    assert get_help('go1') == "go1 help"
