seqtab_nochim_script = os.path.join(config['assnake-dada2']['install_dir'], 'remove_chimeras/seqtab_nochim.R')
rule dada2_nochim:
    input:  '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab__{min_overlap}.rds'
    output: '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab_nochim__{min_overlap}.rds'
    conda: '../dada2.yaml'
    wildcard_constraints:    
        sample_set="[\w\d_-]+",
        # err_params="[\w\d_-]+",
        # min_overlap=" ^[0-9]+$"
    threads: 24
    shell: ('''export LANG=en_US.UTF-8;\nexport LC_ALL=en_US.UTF-8;\n
        Rscript {seqtab_nochim_script} '{input}' '{output}';''') 