from annotated_dataset.inception_client import InceptionClient
from annotated_dataset.export import export
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


# Create client for inception server
inception_client = InceptionClient.create_client(
    host='https://mapa.pangeamt.com/',
    username='xxx',
    password='xxx'
)

# Config
config = {
    'dataset_name': 'MAPA_BG',
    'inception_projects': [
        {
            'name': 'Inception_Test2',
            'use_segmentation_by_newline': True,
            'inception_client': inception_client,
            'use_curated_data': True,
            'allowed_resources': ['Inception_Test2/curation/Test/CURATION_USER']
        }
    ],
    'gold_corpus_preferred_resources': [],
    'export_dir': './'
}


export(config)

