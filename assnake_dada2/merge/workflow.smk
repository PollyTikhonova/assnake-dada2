merge_pooled_script = os.path.join(config['assnake-dada2']['install_dir'], 'merge/merge_pooled.R')
rule dada2_merge_pooled:
    input: 
        dada_1  = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/dadaR1.rds',
        dada_2  = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/dadaR2.rds',
        derep_1 = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/derepR1.rds',
        derep_2 = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/derepR2.rds',
    output:
        mergers = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/mergers__{min_overlap}.rds',
    wildcard_constraints:    
        sample_set="[\w\d_-]+",
        err_params="[\w\d_-]+",
        # min_overlap="^[0-9]+$"
    threads:24
    conda: 'dada2.yaml'
    shell: ('''export LANG=en_US.UTF-8;\nexport LC_ALL=en_US.UTF-8;\n
        Rscript {merge_pooled_script} '{input.derep_1}' '{input.derep_2}'  '{input.dada_1}' '{input.dada_2}' '{output.mergers}';''') 
