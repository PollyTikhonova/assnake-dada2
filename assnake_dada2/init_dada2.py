import assnake.api.loaders
import assnake
from tabulate import tabulate
import click, glob, os
from assnake.utils.general import download_from_url
from assnake.core.config import update_instance_config, read_assnake_instance_config

@click.command('dada2-silva-db', short_help='Initialize Silva database for DADA2')
@click.option('--db-location','-d', 
            help='Where to store DADA2 Silva database. It will take approximately 60 Mb of disk space. silva_nr_v132 will be downloaded', 
            required=False )
@click.pass_obj

def dada2_init(config, db_location):

    db_url = 'https://zenodo.org/record/1172783/files/silva_nr_v132_train_set.fa.gz?download=1'

    if db_location is None: # If no path is provided use default
        instance_config = read_assnake_instance_config()
        db_location = os.path.join(instance_config['assnake_db'], 'dada2')
    
    os.makedirs(db_location, exist_ok=True)
    download_from_url(db_url, os.path.join(db_location, 'silva_nr_v132_train_set.fa.gz'))
    update_instance_config({'dada2-silva_nr_v132': db_location})
