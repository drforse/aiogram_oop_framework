from pathlib import Path
import typing

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram_oop_framework.core.project import Project, ProjectStructure
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PATH = Path.cwd()
PROJECT_NAME = "testbot"
pr: Project = Project(PROJECT_NAME, PATH)
struc: ProjectStructure = ProjectStructure(pr)
struc.include('views')
pr.structure = struc

PROJECT: Project = pr


TELEGRAM_BOT_TOKEN: str = ""

MIDDLEWARES: typing.List[BaseMiddleware.__class__] = []

MEMORY_STORAGE = MemoryStorage()

PARSE_MODE = types.ParseMode.HTML
