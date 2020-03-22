import os
import assnake
from assnake.utils import read_yaml

from assnake_dada2.invocation_commands import filter_and_trim_invocation, dada2_full
from assnake_dada2.init_dada2 import dada2_init



this_dir = os.path.dirname(os.path.abspath(__file__))
snake_module = assnake.SnakeModule(name = 'assnake-dada2', 
                           install_dir = this_dir,
                           snakefiles = ['./dada2.py'],
                           invocation_commands = [filter_and_trim_invocation, dada2_full],
                           initialization_commands = [dada2_init],
                           wc_configs = [read_yaml(os.path.join(this_dir, './wc_config.yaml'))])