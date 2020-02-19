import os
from assnake.api.snake_module import SnakeModule
from assnake.utils import read_yaml

from assnake_dada2.invocation_commands import filter_and_trim_invocation



this_dir = os.path.dirname(os.path.abspath(__file__))
snake_module = SnakeModule(name = 'assnake-dada2', 
                           install_dir = this_dir,
                           snakefiles = ['./dada2.py'],
                           invocation_commands = [filter_and_trim_invocation],
                        #    initialization_commands = [init_remove_human_bbmap],
                           wc_configs = [read_yaml(os.path.join(this_dir, './wc_config.yaml'))])