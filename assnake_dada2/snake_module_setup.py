import os
import assnake

from assnake_dada2.invocation_commands import dada2_full
from assnake_dada2.init_dada2 import dada2_init

snake_module = assnake.SnakeModule(name = 'assnake-dada2', 
                           install_dir = os.path.dirname(os.path.abspath(__file__)),
                           snakefiles = [
                               './assign_taxa/workflow.smk',
                               './remove_chimeras/workflow.smk',
                               './make_seqtab/workflow.smk',
                               './derep_infer_pooled/workflow.smk',
                           ],
                           invocation_commands = [dada2_full],
                           initialization_commands = [dada2_init]
                           )