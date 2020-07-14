Settings
========

Your project settings should be in projects_name/settings.py

PATH: path to folder in which project folder is
PROJECT_NAME: name of the folder of the project

PROJECT: :class:`aiogram_oop_framework.core.project.Project` instance, you don't need to change it, only it's structure field (see in quick-start)

AUTO_REGISTER_VIEWS: does the framework need to register your views automatically or you will do it yourself

TELEGRAM_BOT_TOKEN: token of your bot

MIDDLEWARES: list of your middlewares (from aiogram), must be classes, not instances

MEMORY_STORAGE: memory storage of dispatcher, you may look closer about that in aiogram's docs, or you may not, depends in aiogram's docs

PARSE_MODE: default parse mode for your bot
