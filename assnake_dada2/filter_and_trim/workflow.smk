rule dada2_filter_and_trim:
    input: 
        r1 = '{fs_prefix}/{df}/reads/{preproc}/{sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}/{sample}_R2.fastq.gz',
        params = os.path.join(config['assnake_db'], 'params/dada2/filter_and_trim/{params}.yaml')
    output:
        r1 = '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{params}/{sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{params}/{sample}_R2.fastq.gz'
    log: '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{params}/{sample}.log'
    wildcard_constraints:    
        df="[\w\d_-]+"
    conda: 'dada2.yaml'
    wrapper: "file://" + os.path.join(config['assnake-dada2'], 'filter_trim_wrapper.py')