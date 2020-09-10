from snakemake.shell import shell
import yaml
import os

def get_params_str(params_loc):
    params_str = '{truncLen_f} {trimLeft_l} {maxEE_f} {truncQ} {maxN}'
    with open(snakemake.input.preset, 'r') as stream:
        try:
            par = yaml.safe_load(stream)
            params_str = params_str.format(**par)
        except yaml.YAMLError as exc:
            print(exc)
    
    return params_str

params_str = get_params_str(snakemake.input.preset)
filter_trim_script = os.path.join(snakemake.config['assnake-dada2']['install_dir'], 'filter_and_trim_single/filter_trim_single.R')
shell('''export LANG=en_US.UTF-8;\nexport LC_ALL=en_US.UTF-8;\n
                    Rscript {filter_trim_script} '{snakemake.input.r1}' '{snakemake.output.r1}' {params_str} >{snakemake.log} 2>&1''')
