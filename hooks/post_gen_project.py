import os
import shutil

if {{ cookiecutter.create_virtenv == "y" }}:
    # Check if a virtualenv exists already
    virualenv_name = "dev-{{ cookiecutter.project_name }}"
    bash_command = """cd {{ cookiecutter.project_name }}\nmkvirtualenv {}\npip install -r requirements/dev.txt\npip install -U .""".format(virualenv_name)
    print("""\nSuccess...\nTo create a virtualenv, run the commands:\n\n{}\n""".format(bash_command))

if {{ cookiecutter.script != "y" }}:
    project_root = os.path.realpath(os.path.curdir)
    shutil.rmtree(os.path.join(
        project_root,
        '{{cookiecutter.repo_name}}',
        'scheduler'
    ))