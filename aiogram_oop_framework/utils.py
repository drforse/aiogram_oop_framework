import os
import importlib
import typing

from pathlib import Path
from aiogram_oop_framework.core.project import Project


def import_all_modules_in_project(project: Project):
    """
    import all modules in all directories of the project (defined in project.structure)
    :param project: the project object to find out the project's structure (project.structure) and root directory (project.name)
    :return:
    """
    def foo(tree: dict, startswith: str):
        for directory in tree:
            path: Path = tree[directory]['directory']
            for module in os.listdir(str(path)):
                if module == '__init__.py' or not module.endswith('.py'):
                    # print('continued', module)
                    continue
                name = module.replace('.py', '')
                importlib.import_module(startswith + directory + '.' + name)
                # print(startswith + directory + '.' + name, 'imported')
            foo(tree[directory]['tree'], startswith=startswith + directory + '.')

    try:
        foo(project.structure.directories['root']['tree'], startswith=f'{project.name}.')
    except FileNotFoundError as e:
        raise FileNotFoundError('Check your settings.py project structure settings')


def class_is_original(class_: type, library_name: str) -> bool:
    """

    :param class_: the class to check
    :param library_name: the name of the package of which ORIGINAL or not the class
    :return:
    """
    return class_.__module__.split('.')[0] == library_name


def get_non_original_subclasses(base_class: type, library_name: str) -> typing.List['BaseView.__class__']:
    """
    the classes packages must be imported
    :param base_class: the base class to look for subclasses of
    :param library_name: the name of the package of which NOT ORIGINAL result will be
    :return:
    """
    subclasses = base_class.__subclasses__()
    # print('TestView' in str(subclasses))
    result = []
    if not subclasses:
        return result
    for obj in subclasses:
        if not class_is_original(obj, library_name):
            result.append(obj)
        result += get_non_original_subclasses(obj, library_name)
    return result


def order_views(views: typing.List['BaseView.__class__']) -> typing.ValuesView['BaseView.__class__']:
    unordered = []
    ordered_views = {}
    for view in views:
        if view.index is not None:
            ordered_views[view.index] = view
        else:
            unordered.append(view)

    for i in range(len(views)):
        if not unordered:
            break
        if ordered_views.get(i) is not None:
            continue
        ordered_views[i] = unordered.pop(0)
    ordered_views = dict(sorted(ordered_views.items(), key=lambda x: x[0]))

    return ordered_views.values()
