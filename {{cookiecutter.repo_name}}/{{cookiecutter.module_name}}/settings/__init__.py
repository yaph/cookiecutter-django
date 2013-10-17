try:
    from {{cookiecutter.module_name}}.settings.local import *
except ImportError:
    from {{cookiecutter.module_name}}.settings.base import *
