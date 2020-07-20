make_seqtab_script = os.path.join(config['assnake-dada2'], 'scripts/make_seqtab.R')
rule dada2_make_seqtab:
    input: mergers = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/mergers__{min_overlap}.rds',
    output:          '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab__{min_overlap}.rds'
    conda: 'dada2.yaml'
    wildcard_constraints:    
        sample_set="[\w\d_-]+",
        err_params="[\w\d_-]+",
        # min_overlap="^[0-9]+$"
    shell: ('''export LANG=en_US.UTF-8;\nexport LC_ALL=en_US.UTF-8;\n
        Rscript {make_seqtab_script} '{input.mergers}' '{output}';''') 