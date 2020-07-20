rule dada2_filter_and_trim:
    input: 
        r1 = '{fs_prefix}/{df}/reads/{preproc}/{sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}/{sample}_R2.fastq.gz',
        preset = os.path.join(config['assnake_db'], 'presets/dada2-filter-and-trim/{preset}.yaml')
    output:
        r1 = '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{preset}/{sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{preset}/{sample}_R2.fastq.gz'
    log:     '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{preset}/{sample}.log'
    wildcard_constraints:    
        df="[\w\d_-]+"
    conda: '../dada2.yaml'
    wrapper: "file://" + os.path.join(config['assnake-dada2']['install_dir'], 'filter_and_trim/wrapper.py')