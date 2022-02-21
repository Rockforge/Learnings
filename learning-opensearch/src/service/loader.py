import json
from .pokemon import PokemonService

# Base path for our data
base_path = './pokemon.json/'

index_body = {
    'settings': {
        'index': {
            'number_of_shards': 4
        }
    }
}

def load_indices(client):
    # Create our indices
    # Loop through each index
    for index in PokemonService.indices:
        try:
            # Create already handles if we have a index present
            client.indices.create(
                PokemonService.indices[index], # Name of index
                body=index_body
            )
            print(PokemonService.indices[index]+' created')

        except:
            print(PokemonService.indices[index]+' alredy exists')

def load_data(client):

    for index in PokemonService.indices:
        # The index name is same with the file names
        # found in our data source
        with open(f'{base_path}{index}.json') as data:
            data = json.load(data);

        index_name = f'{index}-index'

        # First, check if the index alread contains data
        response = client.search(
            index = index_name,
            body = {
                'query': {
                    'match_all': {}
                }
            }
        )

        if 'hits' in response:
            print('Data is already present')
            continue

        # Loop through our data
        for item in data:
            client.index(
                index = index_name,
                body = item,
                id = item['id'] if 'id' in item else None,
                refresh = True
            )
