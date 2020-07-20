assign_taxa_script = os.path.join(config['assnake-dada2'], 'scripts/assign_taxa.R')
db_silva_nr_v132 = config.get('dada2-silva_nr_v132', None)
rule dada2_assign_taxa:
    input: '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab_nochim__{min_overlap}.rds'
    output: '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/taxa_{min_overlap}.rds'
    threads: 24
    conda: 'dada2.yaml'
    shell: ("Rscript {assign_taxa_script} '{input}' '{output}' '{db_silva_nr_v132}' {threads}")