from http.client import HTTPException
from fastapi import FastAPI
import validators

from . import schemas
# instantiate FastAPI class
app = FastAPI()

# create exception handling for 400 
def raise_bad_request(msg):
    raise HTTPException(status_code=400, detail=msg)

#
# path op dectorator to associate root path for GET requests
# fastapi listens to root path & tells all incoming get req to go to read_root() fn
# uses uvicorn as server
# GET METHOD
@app.get("/")
def read_root():
    # return string when request to root path is sent
    return 'This is url shortner'

# POST METHOD
@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url)
        raise_bad_request(msg="### URL not valid")
    return f'TODO: Create DB Entry for: {url.target_url}'
