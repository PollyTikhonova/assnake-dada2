import os
from assnake.core.result import Result

result = Result.from_location(name='dada2-filter-and-trim',
                              description='Quality based filtering and trimming from DADA2',
                              result_type = 'preprocessing',
                              input_type='illumina_sample',
                              with_presets=True,
                              preset_file_format='yaml',
                              location=os.path.dirname(os.path.abspath(__file__)))