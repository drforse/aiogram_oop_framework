import click
import logging

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


def initialize_project():
    if not TELEGRAM_BOT_TOKEN:
        raise exceptions.BotTokenNotDefined
    BaseView.bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=PARSE_MODE)
    BaseView.dp = Dispatcher(bot=BaseView.bot, storage=MEMORY_STORAGE)

    for middleware in MIDDLEWARES:
        BaseView.dp.middleware.setup(middleware())

    utils.import_all_modules_in_project(project=PROJECT)
    views = utils.get_non_original_subclasses(BaseView, 'aiogram_oop_framework')

    ordered_views = utils.order_views(views)
    for view in ordered_views:
        view.register()


@main.command()
def start_polling():
    initialize_project()
    executor.start_polling(BaseView.dp)


@main.command()
def start_webhook():
    raise NotImplementedError


@main.command()
def update_structure_from_settings():
    PROJECT.structure.apply_changes()


if __name__ == "__main__":
    main()
