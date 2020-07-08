import os
import importlib
import typing

from pathlib import Path
from aiogram_oop_framework.core.project import Project
from aiogram_oop_framework.views.base import BaseView


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

    foo(project.structure.directories['root']['tree'], startswith=f'{project.name}.')


def class_is_original(class_: type, library_name: str) -> bool:
    """

    :param class_: the class to check
    :param library_name: the name of the package of which ORIGINAL or not the class
    :return:
    """
    return class_.__module__.split('.')[0] == library_name


def get_non_original_subclasses(base_class: type, library_name: str) -> typing.List[type]:
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


def order_views(views: typing.List[BaseView.__class__]) -> typing.List[BaseView.__class__]:
    ordered_views = []
    for view in views:
        if view.index is not None:
            ordered_views.insert(view.index, view)
        else:
            ordered_views.append(view)
    return ordered_views
