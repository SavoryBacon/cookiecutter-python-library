try:
    from .{{cookiecutter.repo_name}} import *
except ImportError:
    pass
__version__='{{ cookiecutter.version }}'
