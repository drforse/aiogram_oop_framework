from pathlib import Path

from aiogram_oop_framework.core.project_files_templates import SETTINGS_PY_TEMPLATE, MANAGE_PY_TEMPLATE


def generate_settings_py(project_name: str, path: Path):
    with open(path, 'w') as f:
        content = SETTINGS_PY_TEMPLATE.replace('$project_name', f'"{project_name}"')
        f.write(content)
    return path


def generate_manage_py(path: Path) -> Path:
    with open(path, 'w') as f:
        f.write(MANAGE_PY_TEMPLATE)
    return path
