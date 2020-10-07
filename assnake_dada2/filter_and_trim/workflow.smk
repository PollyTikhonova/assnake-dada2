from assnake.core.dataset import Dataset

def input_filter_and_trim(wildcards):
    if Dataset(wildcards.df).dataset_type == 'paired-end':
        return [
                '{fs_prefix}/{df}/reads/{preproc}/{sample}_R1.fastq.gz',
                '{fs_prefix}/{df}/reads/{preproc}/{sample}_R2.fastq.gz',
                os.path.join(config['assnake_db'], 'presets/dada2-filter-and-trim/{preset}.yaml')
                ]
    else:
        return [
                '{fs_prefix}/{df}/reads/{preproc}/{sample}_R1.fastq.gz',
                os.path.join(config['assnake_db'], 'presets/dada2-filter-and-trim-single/{preset}.yaml')
                ]

rule dada2_filter_and_trim:
    input: input_filter_and_trim
    output:
        r1 = '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{preset}/{sample}_R1.fastq.gz'
    params:
        r2 = '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{preset}/{sample}_R2.fastq.gz'
        dataset_type=lambda wildcards: Dataset(wildcards.df).dataset_type
    log:     '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{preset}/{sample}.log'
    wildcard_constraints:    
        df="[\w\d_-]+"
    conda: '../dada2.yaml'
    wrapper: "file://" + os.path.join(config['assnake-dada2']['install_dir'], 'filter_and_trim/wrapper.py')

