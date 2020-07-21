import os
from assnake.core.result import Result

result = Result.from_location(name='dada2-learn-errors',
                              description='Learn error profile of provided samples',
                              result_type = 'dada2',
                              input_type='illumina_sample_set',
                              with_presets=True,
                              preset_file_format='yaml',
                              location=os.path.dirname(os.path.abspath(__file__)))