from typing import Union

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from assnake_dada2.snake_module_setup import snake_module

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        snake_module.deploy_module()
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        snake_module.deploy_module()
        install.run(self)


setup(
    name='assnake-dada2',
    version='0.0.6',
    packages=find_packages(),
    entry_points = {
        'assnake.plugins': ['assnake-dada2 = assnake_dada2.snake_module_setup:snake_module']
    },
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
)