from fastapi import FastAPI, HTTPException
from enum import Enum

class BandGenreChoices(Enum):
    ROCK = 'rock'
    METAL = 'metal'
    ELECTRONIC = 'electronic'


app = FastAPI()

BANDS = [
    {
        "id" : 1,
        "name" : "Band 1",
        "genre" : "Rock",
    },
    {
        "id" : 2,
        "name" : "Band 2",
        "genre" : "Electronic",
    },
    {
        "id" : 3,
        "name" : "Band 3",
        "genre" : "Metal",
    },
    {
        "id" : 4,
        "name" : "Band 4",
        "genre" : "Rock",
    },
]



@app.get('/bands')
def index():
    return BANDS

@app.get('/bands/genre/{genre}')
def band(genre : BandGenreChoices):
    return [
        b for b in BANDS if b["genre"].lower() == genre.value
    ]

@app.get('/bands/{band_id}')
def band(band_id : int):
    band = next((b for b in BANDS if b["id"] == band_id), None)
    if band == None:
        raise HTTPException(status_code=404, detail="Band not found")
    else:
        return band
    
    

