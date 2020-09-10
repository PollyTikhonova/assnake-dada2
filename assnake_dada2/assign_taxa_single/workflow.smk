assign_taxa_script = os.path.join(config['assnake-dada2']['install_dir'], 'assign_taxa_single/assign_taxa.R')
db_silva_nr_v132 = config.get('dada2-silva_nr_v132', None)
rule dada2_assign_taxa_single:
    input: '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab_nochim.rds'
    output: '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/taxa.rds'
    threads: 24
    conda: '../dada2.yaml'
    shell: ("Rscript {assign_taxa_script} '{input}' '{output}' '{db_silva_nr_v132}' {threads}")