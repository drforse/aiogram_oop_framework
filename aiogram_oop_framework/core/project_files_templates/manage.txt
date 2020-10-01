import asyncio

import click
import logging

from aiogram import Dispatcher, Bot
from aiogram import executor
from aiogram_oop_framework.views.base import BaseView
from aiogram_oop_framework import utils
from aiogram_oop_framework import exceptions
from aiogram_oop_framework.filters.builtin import *

from .settings import *


logging.basicConfig(level=logging.INFO)


@click.group()
def main():
    """
    This is
    """
    pass


def initialize_project(dispatcher: Dispatcher = None, bot: Bot = None, loop=None) -> typing.Tuple[Dispatcher, Bot]:
    if not TELEGRAM_BOT_TOKEN and not bot:
        raise exceptions.BotTokenNotDefined
    if not dispatcher:
        loop = loop or asyncio.get_event_loop()
        bot = bot or Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=PARSE_MODE)
        dp = dispatcher or Dispatcher(bot=bot, storage=BOT_STORAGE, loop=loop)
    else:
        dp = dispatcher
        bot = bot or dp.bot
    Dispatcher.set_current(dp)

    dp.filters_factory.bind(Entities, event_handlers=[dp.message_handlers, dp.poll_handlers])
    dp.filters_factory.bind(ChatTypeFilter, event_handlers=[dp.message_handlers, dp.callback_query_handlers])
    dp.filters_factory.bind(ChatMemberStatus, event_handlers=[dp.message_handlers, dp.callback_query_handlers])
    dp.filters_factory.bind(PollTypeFilter, event_handlers=[dp.message_handlers, dp.callback_query_handlers, dp.poll_handlers])
    dp.filters_factory.bind(DiceEmoji, event_handlers=[dp.message_handlers, dp.callback_query_handlers])
    dp.filters_factory.bind(FuncFilter)

    utils.import_all_modules_in_project(project=PROJECT)
    views = utils.get_non_original_subclasses(BaseView, 'aiogram_oop_framework')

    for middleware in MIDDLEWARES:
        dp.middleware.setup(middleware())

    ordered_views = utils.order_views(views)
    for view in ordered_views:
        view.bot = view.bot or bot
        if AUTO_REGISTER_VIEWS is True and view.auto_register is True:
            view.register(dp=dp)
    return dp, bot


@main.command()
def start_polling():
    dp, bot = initialize_project()
    if dp.loop:
        executor.start_polling(dp)
    else:
        executor.start_polling(dp, loop=asyncio.get_event_loop())


@main.command()
def start_webhook():
    raise NotImplementedError


if __name__ == "__main__":
    main()
