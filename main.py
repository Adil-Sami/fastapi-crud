from fastapi import FastAPI, HTTPException

app = FastAPI()

BANDS = [
    {
        "id" : 1,
        "name" : "Band 1"
    },
    {
        "id" : 2,
        "name" : "Band 2"
    },
    {
        "id" : 3,
        "name" : "Band 3"
    },
    {
        "id" : 4,
        "name" : "Band 4"
    },
]



@app.get('/')
def index():
    return BANDS

@app.get('/{band_id}')
def band(band_id : int):
    band = next((b for b in BANDS if b["id"] == band_id), None)
    if band == None:
        raise HTTPException(status_code=404, detail="Band not found")
    else:
        return band
    