import assnake.api.loaders
import assnake.api.sample_set
from tabulate import tabulate
import click
from assnake.cli.cli_utils import options_w_params, add_options, generic_command_individual_samples, generate_result_list


@click.command('dada2-filter-and-trim', short_help='Filter and trim your reads with dada2 trimmer')
@add_options(options_w_params)
@click.pass_obj
def filter_and_trim_invocation(config, result = 'dada2-filter-and-trim', **kwargs):
    wc_str = '{fs_prefix}/{df}/reads/{preproc}__dada2fat_{params}/{sample}_R1.fastq.gz'
    sample_set = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    


@click.command('dada2-full', short_help='Execute full dada2 pipeline')

@click.option('--df','-d', help='Name of the dataset', required=True )
@click.option('--preproc','-p', help='Preprocessing to use' )
@click.option('--samples-to-add','-s', 
                help='Samples from dataset to process', 
                default='', 
                metavar='<samples_to_add>', 
                type=click.STRING )
@click.option('--learn-errors-params', 
                help='Parameters for learn errors', 
                default='def',
                type=click.STRING )
@click.option('--min-overlap', 
                help='Minimum overlap when merging reads', 
                default='20',
                type=click.STRING )

@click.pass_obj
def dada2_full(config, df, preproc, samples_to_add, learn_errors_params, min_overlap):
    # check if database initialized
    if config['config'].get('dada2-silva_nr_v132', None) is None:
        click.secho('Silva database not initialized!', fg='red')
        click.echo('run ' + click.style('assnake init dada2-silva-db', bg='blue') + ' and follow instructions')
        exit()
    samples_to_add = [] if samples_to_add == '' else [c.strip() for c in samples_to_add.split(',')]
    df = assnake.api.loaders.load_df_from_db(df)
    config['requested_dfs'] += [df['df']]
    ss = assnake.api.sample_set.SampleSet(df['fs_prefix'], df['df'], preproc, samples_to_add=samples_to_add)

    click.echo(tabulate(ss.samples_pd[['fs_name', 'reads', 'preproc']].sort_values('reads'), 
        headers='keys', tablefmt='fancy_grid'))

    set_name='sample_set'
    ss.prepare_dada2_sample_list(set_name)
    res_list = ['{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{params}/taxa_{len}.rds'.format(
        fs_prefix = df['fs_prefix'].rstrip('\/'),
        df = df['df'],
        sample_set = set_name,
        params = learn_errors_params,
        len = min_overlap
    )]


    if config.get('requests', None) is None:
        config['requests'] = res_list
    else:
        config['requests'] += res_list