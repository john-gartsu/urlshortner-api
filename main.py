# deprecated used in keygen mod
# import secrets

from urllib import request
from fastapi import Depends, FastAPI, HTTPException, Request
# created routes to redirect shortenedURL to target url 
from fastapi.responses import RedirectResponse
import validators
from sqlalchemy.orm import Session
# custom mods
from database import SessionLocal, engine
import crud_ops
import schemas
import models
# instantiate FastAPI class
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    # except:
    #     return f'Error occurred get_db fn'
    finally:
        db.close()
# 
# exception handling:
# 
# create exception handling for 400 
def raise_bad_request(msg):
    raise HTTPException(status_code=400, detail=msg)

# not found exception for handling 404 
def raise_not_found(request):
    message = f"URL '{request.url}' does not exist"
    raise HTTPException(status_code=400, detail=message)

#
# path op dectorator to associate root path for GET requests
# fastapi listens to root path & tells all incoming get req to go to read_root() fn
# uses uvicorn as server
# GET METHOD root
#
@app.get("/")
def read_root():
    # return string when request to root path is sent
    return 'This is url shortner'

# GET method for url_key
@app.get("/{url_key}")
def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    if db_url := crud_ops.get_db_url_by_key(db=db, url_key=url_key):
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)


# POST METHOD
@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    # try:
    if not validators.url(url.target_url):
        raise_bad_request(msg="### The URL is not valid")

    # create db_url using crud_ops fn, get db object back
    db_url = crud_ops.create_db_url(db=db, url=url)
    # add key to request/resp
    db_url.url = db_url.key
    db_url.admin_url = db_url.secret_key

    return db_url
    # except:
    #     return f'### Error: create_url fn error in post request...'
    # return f'TODO: Create DB Entry for: {url.target_url}'

# @local-testing
# db=SessionLocal()
# print(db.query(models.URL).all())