from pathlib import Path

import click

from .core.management.commands.startproject import start_project


@click.group()
def main():
    """
    This is an extender for aiogram to make it more OOP
    """
    pass


@main.command()
@click.argument('project_name')
def startproject(project_name):
    start_project(project_name)
    return


if __name__ == "__main__":
    main()
