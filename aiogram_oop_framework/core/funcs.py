from pathlib import Path
import shutil

from aiogram_oop_framework.core import project_files_templates


def get_settings_py(path: Path, project_name: str) -> Path:
    with open(project_files_templates.SETTINGS_PATH) as f:
        template = f.read()
    path_in_template = '/'.join(str(path.absolute()).replace('\\', '/').split('/')[:-1])
    template = template.replace("$PATH", 'Path("{}")'.format(path_in_template))
    template = template.replace("$PROJECT_NAME", f'"{project_name}"')
    with open(path / "settings.py", 'w') as f:
        f.write(template)
    return path


def get_manage_py(path: Path) -> Path:
    shutil.copyfile(project_files_templates.MANAGE_PATH, path / 'manage.py')
    return path


def get_init_py(path: Path, project_name: str) -> Path:
    with open(project_files_templates.INIT_PATH) as f:
        template = f.read()
    template = template.replace("$PROJECT_NAME", project_name)
    with open(path / '__init__.py', 'w') as f:
        f.write(template)
    return path
