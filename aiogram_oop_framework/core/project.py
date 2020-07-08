from pathlib import Path


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

    def apply_changes(self):
        def foo(tree: dict):
            for directory in tree:
                path: Path = tree[directory]['directory']
                if not path.exists():
                    path.mkdir()
                foo(tree[directory]['tree'])
        foo(self.directories['root']['tree'])


class Project:

    def __init__(self, name: str, path: Path = None):
        self.name: str = name
        self.path: Path = path
        self.structure = None

    def create(self, default=True):
        if not self.path:
            self.path = Path.cwd()
        path = self.path / self.name
        Path.mkdir(path)
        if default:
            self.structure = ProjectStructure(self)
            self.structure.add_dir_to_root('views')
            self.structure.add_dir('views', 'commands')
            self.structure.add_dir('views.commands', 'dev_commands')
            self.structure.add_dir('views.commands', 'user_commands')
            self.structure.apply_changes()
