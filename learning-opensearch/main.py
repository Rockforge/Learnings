from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.service import pokeService


app = FastAPI()

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/pokemon/{pokemon_id}')
def get_pokemon(pokemon_id: int):
    return pokeService.get('pokedex', pokemon_id)['_source']
