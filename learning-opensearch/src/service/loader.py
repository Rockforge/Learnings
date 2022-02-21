from .pokemon import PokemonService

# Base path for our data
base_path = '../../pokemon.json/'

index_body = {
    'settings': {
        'index': {
            'number_of_shards': 4
        }
    }
}

def load_data(client):
    # Create our indeces

    # Loop through each index
    for index in PokemonService.indexes:
        try:
            # Create already handles if we have a index present
            client.indices.create(
                PokemonService.indexes[index], # Name of index
                body=index_body
            )
            print(PokemonService.indexes[index]+' created')

        except:
            print(PokemonService.indexes[index]+' alredy exists')
