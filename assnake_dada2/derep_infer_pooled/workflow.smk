rule dada2_derep_infer_pooled:
    input: 
        samples_list = '{fs_prefix}/{df}/dada2/{sample_set}/samples.tsv',
        err          = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/err{strand}.rds'
    output:
        infered      = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/dada{strand}.rds',
        derep        = '{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/derep{strand}.rds',
    threads: 24
    conda: 'dada2.yaml'
    wrapper: "file://" + os.path.join(config['assnake-dada2']['install_dir'], 'derep_infer_pooled/infer_pooled_wrapper.py') 