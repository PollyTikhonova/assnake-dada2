import assnake.api.loaders
import assnake.api.sample_set
from tabulate import tabulate
import click


@click.command('dada2-filter-and-trim', short_help='Filter and trim your reads')

@click.option('--df','-d', help='Name of the dataset', required=True )
@click.option('--preproc','-p', help='Preprocessing to use' )
@click.option('--samples-to-add','-s', 
                help='Samples from dataset to process', 
                default='', 
                metavar='<samples_to_add>', 
                type=click.STRING )
@click.option('--params', 
                help='Parameters to use', 
                default='def',
                type=click.STRING )
@click.pass_obj
def filter_and_trim_invocation(config, df, preproc, samples_to_add, params):
    samples_to_add = [] if samples_to_add == '' else [c.strip() for c in samples_to_add.split(',')]
    df = assnake.api.loaders.load_df_from_db(df)
    config['requested_dfs'] += [df['df']]
    ss = assnake.api.sample_set.SampleSet(df['fs_prefix'], df['df'], preproc, samples_to_add=samples_to_add)

    click.echo(tabulate(ss.samples_pd[['fs_name', 'reads', 'preproc']].sort_values('reads'), 
        headers='keys', tablefmt='fancy_grid'))
    res_list = []

    for s in ss.samples_pd.to_dict(orient='records'):
        preprocessing = s['preproc']
        res_list.append( '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{params}/{sample}_R1.fastq.gz'.format(
            fs_prefix = s['fs_prefix'].rstrip('\/'),
            df = s['df'],
            preproc = preprocessing,
            sample = s['fs_name'],
            params = params
        ))

    if config.get('requests', None) is None:
        config['requests'] = res_list
    else:
        config['requests'] += res_list