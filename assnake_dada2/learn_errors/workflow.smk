rule dada2_learn_errors:
    input: 
        samples_list = '{fs_prefix}/{df}/dada2/{sample_set}/samples.tsv',
        params = os.path.join(config['assnake_db'], 'params/dada2/learn_errors/{preset}.yaml')
    output:
        err          = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{preset}/err{strand}.rds'
    log:               '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{preset}/err{strand}.log'
    threads: 12
    conda: 'dada2.yaml'
    wrapper: "file://" + os.path.join(config['assnake-dada2']['install_dir'], 'learn_errors_wrapper.py')