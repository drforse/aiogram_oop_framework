import os
import importlib
import typing
from dataclasses import dataclass
from pathlib import Path

from aiogram import Dispatcher

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


@dataclass
class CommandFunc:
    commands: typing.List[str]
    handler: typing.Awaitable


@dataclass
class CommandHandlers:
    views: typing.List['BaseView.__class__']
    funcs: typing.List[CommandFunc]


def get_command_handlers(dp: Dispatcher = None) -> CommandHandlers:
    from aiogram.dispatcher.filters import Command
    from aiogram_oop_framework.views.base import BaseView
    dp = dp or Dispatcher.get_current()
    result = CommandHandlers([], [])
    for handler in (dp.message_handlers.handlers + dp.edited_message_handlers.handlers +
                    dp.channel_post_handlers.handlers + dp.edited_channel_post_handlers.handlers):
        for fltr in handler.filters:
            if not isinstance(fltr.filter, Command):
                continue
            commands = fltr.filter.commands
            if hasattr(handler.handler, "__self__") and issubclass(handler.handler.__self__, BaseView):
                result.views.append(handler.handler.__self__)
            else:
                result.funcs.append(CommandFunc(commands, handler.handler))
    return result


def get_help(command: str) -> str:
    """
    looks for help in all registered handlers
    returns handler.__self__.get_help() if handler is method else handler.__doc__
    :param command: str - command, for ex.: command="start"
    :return: str
    """
    command_handlers = get_command_handlers()
    for handler in command_handlers.views:
        if command in handler.commands:
            try:
                help_ = handler.get_help() or handler.command_description
            except AttributeError:
                help_ = handler.__doc__
            if help_:
                return help_
    for handler in command_handlers.funcs:
        if command in handler.commands:
            help_ = handler.handler.__doc__
            if help_:
                return help_


class Commands:
    def __init__(self, dp: Dispatcher = None):
        self._dp = dp or Dispatcher.get_current()
        self._commands_dict = {}

    def find_all_commands(self, only_views: bool = True):
        commands_handlers = get_command_handlers(self._dp)
        for handler in commands_handlers.views:
            for command in handler.commands:
                if self._commands_dict.get(command):
                    continue
                self._commands_dict[command] = handler.command_description or handler.get_help()
        if only_views:
            return self
        for handler in commands_handlers.funcs:
            for command in handler.commands:
                if self._commands_dict.get(command):
                    continue
                self._commands_dict[command] = handler.handler.__doc__
        return self

    def __getattr__(self, item):
        result = self._commands_dict.get(item)
        if result:
            return result
        raise AttributeError(f"'Commands' object has no attribute '{item}'")

    def __getitem__(self, item):
        result = self._commands_dict.get(item)
        if result:
            return result
        raise KeyError(item)

    def __iter__(self):
        yield from self._commands_dict

    def __len__(self, other):
        return len(self._commands_dict)

    def __str__(self):
        return str(self._commands_dict)

    def format(self, prefix: str = "/", separator: str = ": ") -> str:
        return "\n".join(
            f"{prefix}{command}{separator}{description}"
            for command, description in self._commands_dict.items()
        )
