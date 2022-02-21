from src.opensearch import client
from .pokemon import PokemonService
from . import loader

# Run this loader
loader.load_data(client)
