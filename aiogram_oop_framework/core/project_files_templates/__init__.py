from pathlib import Path

path = __file__.replace('__init__.py', '')
path = Path(path)
print(path)
with open(path / 'manage.txt') as f:
    MANAGE_PY_TEMPLATE = f.read()
with open(path / 'settings.txt') as f:
    SETTINGS_PY_TEMPLATE = f.read()


__all__ = ['MANAGE_PY_TEMPLATE', 'SETTINGS_PY_TEMPLATE']
