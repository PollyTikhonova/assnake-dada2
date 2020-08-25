track_reads_script = os.path.join(config['assnake-dada2']['install_dir'], 'track_reads/track_reads.R')

rule dada2_track_reads:
    input:  
        seqtab_nochim = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab_nochim__{min_overlap}.rds',
        seqtab  = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab__{min_overlap}.rds',
        mergers = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/mergers__{min_overlap}.rds',
        derepR1 = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/derepR1.rds',
        derepR2 = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/derepR2.rds',
        dadaR1  = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/dadaR1.rds',
        dadaR2  = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/dadaR2.rds',
        taxa    = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/taxa_{min_overlap}.rds'
    output:     '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{err_params}/seqtab_nochim__{min_overlap}.reads_count.tsv'
    conda: '../dada2.yaml'
    shell: ("Rscript {track_reads_script} '{input.seqtab_nochim}' '{input.seqtab}' '{input.mergers}' '{input.derepR1}' '{input.derepR2}' '{input.dadaR1}' '{input.dadaR2}' '{output}'")