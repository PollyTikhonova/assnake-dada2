rule dada2_filter_and_trim_single:
    input: 
        r1 = '{fs_prefix}/{df}/reads/{preproc}/{sample}_R1.fastq.gz',
        preset = os.path.join(config['assnake_db'], 'presets/dada2-filter-and-trim-single/{preset}.yaml')
    output:
        r1 = '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{preset}/{sample}_R1.fastq.gz',
    log:     '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{preset}/{sample}.log'
    wildcard_constraints:    
        df="[\w\d_-]+"
    conda: '../dada2.yaml'
    wrapper: "file://" + os.path.join(config['assnake-dada2']['install_dir'], 'filter_and_trim_single/wrapper.py')