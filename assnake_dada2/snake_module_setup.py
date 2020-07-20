import os
import assnake

# from assnake_dada2.invocation_commands import filter_and_trim_invocation, dada2_full
from assnake_dada2.init_dada2 import dada2_init

snake_module = assnake.SnakeModule(name = 'assnake-dada2', 
                           install_dir = os.path.dirname(os.path.abspath(__file__)),
                           initialization_commands = [dada2_init]
                           )