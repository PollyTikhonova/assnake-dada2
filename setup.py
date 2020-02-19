from typing import Union

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from assnake.utils import get_config_loc, load_config_file
import os, shutil
import click


def prepare_params():
    if os.path.isfile(get_config_loc()):
        config = load_config_file()
        os.makedirs(os.path.join(config['assnake_db'], 'params/dada2/filter_and_trim'), exist_ok=True)
        os.makedirs(os.path.join(config['assnake_db'], 'params/dada2/learn_errors'), exist_ok=True)
        os.makedirs(os.path.join(config['assnake_db'], 'params/dada2/merge'), exist_ok=True)

        shutil.copyfile('./assnake_dada2/params/filter_and_trim/def.yaml', os.path.join(config['assnake_db'], 'params/dada2/filter_and_trim/def.yaml'))
        shutil.copyfile('./assnake_dada2/params/learn_errors/def.yaml', os.path.join(config['assnake_db'], 'params/dada2/learn_errors/def.yaml'))
        shutil.copyfile('./assnake_dada2/params/merge/10.yaml', os.path.join(config['assnake_db'], 'params/dada2/merge/10.yaml'))
        shutil.copyfile('./assnake_dada2/params/merge/20.yaml', os.path.join(config['assnake_db'], 'params/dada2/merge/20.yaml'))

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        prepare_params()
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        prepare_params()
        install.run(self)


setup(
    name='assnake-dada2',
    version='0.0.1',
    packages=find_packages(),
    entry_points = {
        'assnake.plugins': ['assnake-dada2 = assnake_dada2.snake_module_setup:snake_module']
    },
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
)