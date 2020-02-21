import assnake.api.loaders
import assnake.api.sample_set
from tabulate import tabulate
import click, glob, os
from assnake.utils import download_from_url, update_config, load_config_file

@click.command('dada2-silva-db', short_help='Initialize Silva database for DADA2')
@click.option('--db-location','-d', 
            help='Where to store DADA2 Silva database. It will take approximately 60 Mb of disk space. silva_nr_v132 will be downloaded', 
            required=False )
@click.pass_obj

def dada2_init(config, db_location):

    db_url = 'https://zenodo.org/record/1172783/files/silva_nr_v132_train_set.fa.gz?download=1'

    if db_location is None: # If no path is provided use default
        config = load_config_file()
        db_location = os.path.join(config['assnake_db'], 'dada2')
    
    os.makedirs(db_location, exist_ok=True)
    download_from_url(db_url, os.path.join(db_location, 'silva_nr_v132_train_set.fa.gz'))
    update_config({'dada2-silva_nr_v132': db_location})
