rule dada2_learn_errors_single:
    input: 
        samples_list = '{fs_prefix}/{df}/dada2/{sample_set}/samples.tsv',
        preset = os.path.join(config['assnake_db'], 'presets/dada2-learn-errors/{preset}.yaml')
    output:
        err          = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{preset}/err.rds'
    log:               '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{preset}/err.log'
    threads: 12
    conda: '../dada2.yaml'
    wrapper: "file://" + os.path.join(config['assnake-dada2']['install_dir'], './learn_errors_single/learn_errors_wrapper.py')