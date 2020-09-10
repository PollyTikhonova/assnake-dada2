rule dada:
    input: 
        samples_list = '{fs_prefix}/{df}/dada2/{sample_set}/samples.tsv',
        err          = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/err.rds'
    output:
        dada      = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/dada.rds',
        derep        = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/derep.rds',
    threads: 24
    conda: '../dada2.yaml'
    wrapper: "file://" + os.path.join(config['assnake-dada2']['install_dir'], 'dada/dada_wrapper.py') 