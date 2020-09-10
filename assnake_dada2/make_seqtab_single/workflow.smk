make_seqtab_script = os.path.join(config['assnake-dada2']['install_dir'], 'make_seqtab_single/make_seqtab_single.R')
rule dada2_make_seqtab_single:
    input: dada = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/dada.rds',
    output:          '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab.rds'
    conda: '../dada2.yaml'
    wildcard_constraints:    
        sample_set="[\w\d_-]+",
        # err_params="[\w\d_-]+",
        # min_overlap="^[0-9]+$"
    shell: ('''export LANG=en_US.UTF-8;\nexport LC_ALL=en_US.UTF-8;\n
        Rscript {make_seqtab_script} '{input.dada}' '{output}';''') 