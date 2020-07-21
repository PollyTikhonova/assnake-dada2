import os
from assnake.core.result import Result

result = Result.from_location(name='dada2-merge',
                              description='Merge strands of your samples with DADA2',
                              result_type = 'dada2',
                              input_type='illumina_sample_set',
                              with_presets=True,
                              preset_file_format='yaml',
                              location=os.path.dirname(os.path.abspath(__file__)))