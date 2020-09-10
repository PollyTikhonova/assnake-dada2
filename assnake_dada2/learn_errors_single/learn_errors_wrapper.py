from snakemake.shell import shell
import yaml
import os

def get_params_str(params_loc):
    params_str = "'{randomize}' {MAX_CONSIST}"
    with open(snakemake.input.preset, 'r') as stream:
        try:
            par = yaml.safe_load(stream)
            params_str = params_str.format(**par)
        except yaml.YAMLError as exc:
            print(exc)
    
    return params_str

params_str = get_params_str(snakemake.input.preset)
learn_errors_script = os.path.join(snakemake.config['assnake-dada2']['install_dir'], 'learn_errors_single/learn_errors_single.R')
shell('''export LANG=en_US.UTF-8;\nexport LC_ALL=en_US.UTF-8;\n
        Rscript  {learn_errors_script} '{snakemake.input.samples_list}' \
            '{snakemake.output.err}' {params_str} {snakemake.threads} > {snakemake.log} 2>&1''')
