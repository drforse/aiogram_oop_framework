from aiogram_oop_framework.core import project
from aiogram_oop_framework.core.funcs import *


def start_project(project_name):
    pr = project.Project(project_name)
    pr.create()
    settings_path = Path(pr.name)
    manage_path = Path(pr.name)
    get_settings_py(settings_path, pr.name)
    get_manage_py(manage_path)
