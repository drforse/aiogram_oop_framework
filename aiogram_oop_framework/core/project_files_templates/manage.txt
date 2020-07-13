import click
import logging
import asyncio

from aiogram import Dispatcher, Bot
from aiogram import executor
from aiogram_oop_framework.views.base import BaseView
from aiogram_oop_framework import utils
from aiogram_oop_framework import exceptions

from .settings import *


logging.basicConfig(level=logging.INFO)


@click.group()
def main():
    """
    This is
    """
    pass


def initialize_project(dispatcher: Dispatcher = None, bot: Bot = None) -> typing.Tuple[Dispatcher, Bot]:
    if not TELEGRAM_BOT_TOKEN and not bot:
        raise exceptions.BotTokenNotDefined
    if not dispatcher:
        bot = bot or Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=PARSE_MODE)
        dp = dispatcher or Dispatcher(bot=bot, storage=MEMORY_STORAGE)
    else:
        dp = dispatcher
        bot = bot or dp.bot

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
    executor.start_polling(dp)


@main.command()
def start_webhook():
    raise NotImplementedError


if __name__ == "__main__":
    main()
