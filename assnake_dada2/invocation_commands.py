import assnake.api.loaders
import assnake
from tabulate import tabulate
import click
from assnake.core.sample_set import generic_command_dict_of_sample_sets, generate_result_list
from assnake.core.command_builder import sample_set_construction_options, add_options
from assnake.core.dataset import Dataset
import os, datetime 
import pandas as pd
from assnake.core.result import Result


@click.command('dada2-full', short_help='Execute full dada2 pipeline')
@add_options(sample_set_construction_options)
@click.option('--sample-set-name', 
                help='Name of your sample set', 
                default='',
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
def dada2_full(config, sample_set_name, learn_errors_params, min_overlap, **kwargs):
    # check if database initialized 
    if config['config'].get('dada2-silva_nr_v132', None) is None:
        click.secho('Silva database not initialized!', fg='red')
        click.echo('run ' + click.style('assnake init dada2-silva-db', bg='blue') + ' and follow instructions')
        exit()


    # load sample set     
    sample_set_dict = generic_command_dict_of_sample_sets(config,  **kwargs)
    for sample_set_name, sample_set in sample_set_dict.items():
        if Dataset(list(set(sample_set['df']))[0]).dataset_type == 'paired-end':
            learn_errors_result = Result.get_result_by_name('dada2-learn-errors')
            learn_errors_preset = learn_errors_result.preset_manager.find_preset_by_name(learn_errors_params)

            if learn_errors_preset is not None:
                pass
            else:
                click.secho('NO SUCH PRESET', fg='red')
                exit()
            # Prepare sample set file
            res_list, destroy_if_not_run = prepare_sample_set_tsv_and_get_results(sample_set, sample_set_name, wc_config = config['wc_config'], learn_errors_params = learn_errors_preset['full_name'], min_overlap = min_overlap)
        else:
            learn_errors_result = Result.get_result_by_name('dada2-learn-errors-single')
            learn_errors_preset = learn_errors_result.preset_manager.find_preset_by_name(learn_errors_params)
            if learn_errors_preset is not None:
                pass
                # learn_errors_params = learn_errors_preset['full_name']
            else:
                click.secho('NO SUCH PRESET', fg='red')
                exit()
            # Prepare sample set file
            res_list, destroy_if_not_run = prepare_sample_set_tsv_and_get_results_single(sample_set, sample_set_name, wc_config = config['wc_config'], learn_errors_params = learn_errors_preset['full_name'])

        config['requests'] += res_list
        if 'requests_storage' not in config:
            config['requests_storage'] = {}
        if kwargs['df'] not in config['requests_storage']:
            config['requests_storage'][kwargs['df']] = {}
        if "dada2-full" not in config['requests_storage'][kwargs['df']]:
            config['requests_storage'][kwargs['df']]["dada2-full"] = []
        config['requests_storage'][kwargs['df']]["dada2-full"] += res_list
        if 'destroy_if_not_run' not in config:
            config['destroy_if_not_run'] = {'directories':[], 'files':[]}
        if 'directories' not in config['destroy_if_not_run']:
            config['destroy_if_not_run']['directories'] = []
        if 'files' not in config['destroy_if_not_run']:
            config['destroy_if_not_run']['files'] = []
        config['destroy_if_not_run']['directories'] += destroy_if_not_run['directories']
        config['destroy_if_not_run']['files'] += destroy_if_not_run['files']

def prepare_sample_set_tsv_and_get_results(sample_set, sample_set_name, wc_config,  **kwargs):
    destroy_if_not_run = {'directories':[], 'files':[]}

    dfs = list(set(sample_set['df']))
    if len(dfs) == 1:
        fs_prefix = list(set(sample_set['fs_prefix']))[0]

    dada2_set_dir_wc = '{fs_prefix}/{df}/dada2/{sample_set_name}'
    dada2_set_dir = '{fs_prefix}/{df}/dada2/{sample_set_name}/'.format(fs_prefix = fs_prefix, df = dfs[0], sample_set_name = sample_set_name)
    # from string import Formatter
    # import string
    # field_names = [name for text, name, spec, conv in string.Formatter().parse(dada2_set_dir_wc)]

    # print(field_names)

    # lst = { }

    # print(dada2_set_dir_wc.format( **{key:value for key,value in kwargs.items() if key in field_names} ))

    dada2_dicts = []
    for s in sample_set.to_dict(orient='records'):
        # print(s)
        dada2_dicts.append(dict(mg_sample=s['df_sample'],
        R1 = wc_config['fastq_gz_file_wc'].format(fs_prefix=s['fs_prefix'], df=s['df'], preproc=s['preproc'], df_sample = s['df_sample'], strand = 'R1'), 
        R2 = wc_config['fastq_gz_file_wc'].format(fs_prefix=s['fs_prefix'], df=s['df'], preproc=s['preproc'], df_sample = s['df_sample'], strand = 'R2'),
        # merged = sample_set.wc_config['dada2_merged_wc'].format(prefix=s['fs_prefix'], df=s['df'], preproc=s['preproc'], sample = s['fs_name'], sample_set = set_name)
        ))
    if not os.path.exists(dada2_set_dir):
        os.makedirs(dada2_set_dir, exist_ok=True)
        destroy_if_not_run['directories'].append(dada2_set_dir)

    dada2_df = pd.DataFrame(dada2_dicts)
    if not os.path.isfile(os.path.join(dada2_set_dir, 'samples.tsv')):
        dada2_df.to_csv(os.path.join(dada2_set_dir, 'samples.tsv'), sep='\t', index=False)
        destroy_if_not_run['files'].append(os.path.join(dada2_set_dir, 'samples.tsv'))

    res_list = ['{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{learn_errors_params}/taxa_{min_overlap}.rds'.format(
        fs_prefix = fs_prefix,
        df = dfs[0],
        sample_set = sample_set_name,
        learn_errors_params = kwargs['learn_errors_params'],
        min_overlap = kwargs['min_overlap']
    )]

    return res_list, destroy_if_not_run



@click.command('dada2-full-single', short_help='Execute full dada2 pipeline for single-end reads')
@add_options(sample_set_construction_options)
@click.option('--sample-set-name', 
                help='Name of your sample set', 
                default='',
                type=click.STRING )
@click.option('--learn-errors-params', 
                help='Parameters for learn errors', 
                default='def',
                type=click.STRING )

# @click.pass_obj
# def dada2_full_single(config, sample_set_name, learn_errors_params, **kwargs):

#     # check if database initialized
#     if config['config'].get('dada2-silva_nr_v132', None) is None:
#         click.secho('Silva database not initialized!', fg='red')
#         click.echo('run ' + click.style('assnake init dada2-silva-db', bg='blue') + ' and follow instructions')
#         exit()
#     print(kwargs)

#     # load sample set     
#     sample_set_dict = generic_command_dict_of_sample_sets(config,  **kwargs)
#     for sample_set_name, sample_set in sample_set_dict.items():
#         learn_errors_result = Result.get_result_by_name('dada2-learn-errors-single')
#         learn_errors_preset = learn_errors_result.preset_manager.find_preset_by_name(learn_errors_params)
#         if learn_errors_preset is not None:
#             learn_errors_params = learn_errors_preset['full_name']
#         else:
#             click.secho('NO SUCH PRESET', fg='red')
#             exit()
#         # Prepare sample set file
#         res_list = prepare_sample_set_tsv_and_get_results_single(sample_set, sample_set_name, wc_config = config['wc_config'], learn_errors_params = learn_errors_params)

#         config['requests'] += res_list
#         if 'requests_storage' not in config:
#             config['requests_storage'] = {}
#         if kwargs['df'] not in config['requests_storage']:
#             config['requests_storage'][kwargs['df']] = {}
#         if "dada2-full" not in config['requests_storage'][kwargs['df']]:
#             config['requests_storage'][kwargs['df']]["dada2-full"] = []
#         config['requests_storage'][kwargs['df']]["dada2-full"] += res_list

def prepare_sample_set_tsv_and_get_results_single(sample_set, sample_set_name, wc_config,  **kwargs):

    destroy_if_not_run = {'directories':[], 'files':[]}
    dfs = list(set(sample_set['df']))
    if len(dfs) == 1:
        fs_prefix = list(set(sample_set['fs_prefix']))[0]

    dada2_set_dir_wc = '{fs_prefix}/{df}/dada2/{sample_set_name}'
    dada2_set_dir = '{fs_prefix}/{df}/dada2/{sample_set_name}/'.format(fs_prefix = fs_prefix, df = dfs[0], sample_set_name = sample_set_name)
    from string import Formatter
    import string
    field_names = [name for text, name, spec, conv in string.Formatter().parse(dada2_set_dir_wc)]

    # print(field_names)

    # lst = { }

    # print(dada2_set_dir_wc.format( **{key:value for key,value in kwargs.items() if key in field_names} ))

    dada2_dicts = []
    for s in sample_set.to_dict(orient='records'):
        # print(s)
        dada2_dicts.append(dict(mg_sample=s['df_sample'],
        R1 = wc_config['fastq_gz_file_wc'].format(fs_prefix=s['fs_prefix'], df=s['df'], preproc=s['preproc'], df_sample = s['df_sample'], strand = 'R1'), 
        # merged = sample_set.wc_config['dada2_merged_wc'].format(prefix=s['fs_prefix'], df=s['df'], preproc=s['preproc'], sample = s['fs_name'], sample_set = set_name)
        ))
    if not os.path.exists(dada2_set_dir):
        os.makedirs(dada2_set_dir, exist_ok=True)
        destroy_if_not_run['directories'].append(dada2_set_dir)

    dada2_df = pd.DataFrame(dada2_dicts)
    if not os.path.isfile(os.path.join(dada2_set_dir, 'samples.tsv')):
        dada2_df.to_csv(os.path.join(dada2_set_dir, 'samples.tsv'), sep='\t', index=False)
        destroy_if_not_run['files'].append(os.path.join(dada2_set_dir, 'samples.tsv'))

    res_list = ['{fs_prefix}/{df}/dada2/{sample_set}/learn_erros__{learn_errors_params}/taxa.rds'.format(
        fs_prefix = fs_prefix,
        df = dfs[0],
        sample_set = sample_set_name,
        learn_errors_params = kwargs['learn_errors_params']
    )]

    return res_list, destroy_if_not_run