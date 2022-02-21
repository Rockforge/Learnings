from src.opensearch import client
from .pokemon import PokemonService
from . import loader

# Run this loader
# Loads data and such
loader.load_indices(client)
loader.load_data(client)

pokeService = PokemonService(client)
