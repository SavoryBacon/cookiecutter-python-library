if {{ cookiecutter.create_virtenv == "y" }}:
    # Check if a virtualenv exists already
    virualenv_name = "{{ cookiecutter.project_name }}-dev"
    bash_command = """cd {{ cookiecutter.project_name }}\nmkvirtualenv {}\npip install -r requirements/dev.txt""".format(virualenv_name)
    print("""\nSuccess...\nTo create a virtualenv, run the commands:\n\n{}\n""".format(bash_command))
