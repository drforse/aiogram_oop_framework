from aiogram import Dispatcher, Bot

from aiogram_oop_framework.views import CommandView, MessageView
from aiogram_oop_framework.utils import get_help, Commands


bot = Bot("34342323:sdfvcawfeedfr")
dp = Dispatcher(bot)


class Start(CommandView):
    """start help"""
    commands = ['start']
    help_text = "overrited start help"
    show_in_commands = True

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        return


class Help(CommandView):
    """help help"""
    update_type = 'edited_message'
    commands = ['help']
    show_in_commands = True

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        return


class MView(MessageView):
    """cancel help"""
    commands = ['cancel']
    short_description = "cancel description"
    show_in_commands = True

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        return


class M1View(MessageView):
    """cancel1 help"""
    commands = ['cancel']
    show_in_commands = True

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        return


class M2View(MessageView):
    """gogogogogogo help"""
    commands = ['gogogogogogo']
    short_description = "gg"
    show_in_commands = False


Start.register(dp)
Help.register(dp)
MView.register(dp)
M1View.register(dp)
M2View.register(dp)


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


def test_get_help():
    Dispatcher.set_current(dp)
    assert get_help('start') == "overrited start help"
    assert get_help('cancel') == "cancel help"
    assert get_help('go') == "go help"
    assert get_help('go1') == "go1 help"


def test_commands_util():
    Dispatcher.set_current(dp)
    commands = Commands()
    commands.find_all_commands(only_views=False)
    assert commands._commands_dict == {"start": "overrited start help",
                                       "help": "help help",
                                       "cancel": "cancel description",
                                       "go": "go help",
                                       "go1": "go1 help",
                                       "gogogogogogo": "gg"}
    assert commands.start == "overrited start help"
    assert commands["help"] == "help help"
    commands_list = [i for i in commands]
    for command in ["start", "help", "cancel", "go1", "go", "gogogogogogo"]:
        assert command in commands_list
    assert commands.format() == "/start: overrited start help\n/cancel: cancel description\n/gogogogogogo: gg\n/help: help help\n/go1: go1 help\n/go: go help"


def test_commands_util_only_views():
    Dispatcher.set_current(dp)
    commands = Commands()
    commands.find_all_commands()
    assert commands._commands_dict == {"start": "overrited start help",
                                       "help": "help help",
                                       "cancel": "cancel description",
                                       "gogogogogogo": "gg"}
    assert commands.start == "overrited start help"
    assert commands["help"] == "help help"
    commands_list = [i for i in commands]
    for command in ["start", "help", "cancel", "gogogogogogo"]:
        assert command in commands_list
    assert commands.format() == "/start: overrited start help\n/cancel: cancel description\n/gogogogogogo: gg\n/help: help help"


def test_commands_util_with_filter():
    Dispatcher.set_current(dp)
    commands = Commands()
    commands.find_all_commands(only_views=False, filter_=lambda v: v.show_in_commands)
    print(commands._commands_dict)
    assert commands._commands_dict == {"start": "overrited start help",
                                       "help": "help help",
                                       "cancel": "cancel description",
                                       "go": "go help",
                                       "go1": "go1 help"}
    assert commands.start == "overrited start help"
    assert commands["help"] == "help help"
    commands_list = [i for i in commands]
    for command in ["start", "help", "cancel", "go1", "go"]:
        assert command in commands_list
    assert commands.format() == "/start: overrited start help\n/cancel: cancel description\n/help: help help\n/go1: go1 help\n/go: go help"
