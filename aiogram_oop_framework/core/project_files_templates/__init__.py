from pathlib import Path

parent = Path(__file__).parent
INIT_PATH = parent / '__init__.txt'
MANAGE_PATH = parent / 'manage.txt'
SETTINGS_PATH = parent / 'settings.txt'


__all__ = ['INIT_PATH', 'MANAGE_PATH', 'SETTINGS_PATH']


# with open('__init__.txt', 'r') as f:
#     INIT_PY = f.read()
# with open('manage.txt', 'r') as f:
#     MANAGE_PY = f.
