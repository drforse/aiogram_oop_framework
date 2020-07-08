from pathlib import Path

from aiogram_oop_framework.core.funcs import get_init_py


class ProjectStructure:
    def __init__(self, project: 'Project'):
        self.root: Path = project.path / project.name
        self.directories = {'root': {'directory': self.root, 'tree': {}}}

    def add_dir_to_root(self, name: str):
        path = self.root / name
        self.directories['root']['tree'][name] = {'directory': path, 'tree': {}}

    def add_dir(self, path: str, name: str):
        """

        :param path: any_dir.another_dir (found in project root)
        :param name: dir_name
        :return:
        """
        path_steps = path.split('.')
        current_step = self.directories['root']
        for step in path_steps:
            current_step = current_step['tree'][step]
        path = current_step['directory'] / name
        current_step['tree'][name] = {'directory': path, 'tree': {}}

    def include(self, path: str):
        """
        it will create the folders in the path which aren't created yet
        :param path: any_dir.another_dir (found in project root)
        :return:
        """
        path_steps = path.split('.')
        current_step = self.directories['root']
        for step in path_steps:
            current_step_struc = current_step['tree'].get(step)
            if current_step_struc:
                current_step = current_step_struc
            else:
                current_step['tree'][step] = {'directory': current_step['directory'] / step, 'tree': {}}
                current_step = current_step['tree'][step]

    def apply_changes(self):
        def foo(tree: dict):
            for directory in tree:
                path: Path = tree[directory]['directory']
                if not path.exists():
                    path.mkdir()
                    with open(path / '__init__.py', 'w') as f:
                        f.write('\n')
                foo(tree[directory]['tree'])
        foo(self.directories['root']['tree'])


class Project:

    def __init__(self, name: str, path: Path = None):
        self.name: str = name
        self.path: Path = path
        self.structure: ProjectStructure = None

    def create(self, default=True):
        if not self.path:
            self.path = Path.cwd()
        path = self.path / self.name
        Path.mkdir(path)
        get_init_py(path, self.name)
        if default and not self.structure:
            self.structure = ProjectStructure(self)
            self.structure.include('views')
            self.structure.apply_changes()
        if self.structure:
            self.structure.apply_changes()
