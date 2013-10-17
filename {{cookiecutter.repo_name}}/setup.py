try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='{{cookiecutter.module_name}}',
    version='0.1',
    description='{{cookiecutter.description}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    packages=find_packages(),
    scripts=['manage.py'],
    classifiers=(
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
    ),
)
