class PokemonService:

    """Pokemon Service"""

    # The list of indices in our OpenSearch
    indices = {
        'pokedex': 'pokedex-index',
        'items': 'items-index',
        'moves': 'moves-index',
        'types': 'types-index',
    }

    def __init__(self, client):
        self.client = client

    def get(self, index: str, id: int):
        """Get data

        Parameters
        ----------
        index : str
            The index to use
        id : int
            The document ID of the data
        """

        if index not in self.indices:
            raise Exception

        return client.get(self.indices[index], id)
