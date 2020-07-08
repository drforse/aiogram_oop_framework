from aiogram_oop_framework.core import project
from aiogram_oop_framework.core.funcs import *


def start_project(project_name):
    pr = project.Project(project_name)
    pr.create()
    settings_path = Path(pr.name) / 'settings.py'
    manage_path = Path(pr.name) / 'manage.py'
    generate_settings_py(project_name, settings_path)
    generate_manage_py(manage_path)
