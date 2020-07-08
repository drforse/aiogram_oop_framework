from ... import project


def start_project(project_name):
    pr = project.Project(project_name)
    pr.create()
