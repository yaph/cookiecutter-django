try:
    from {{cookiecutter.repo_name}}.settings.local import *
except ImportError:
    from {{cookiecutter.repo_name}}.settings.base import *
