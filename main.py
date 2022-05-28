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
    except:
        return f'Error occurred get_db fn'
    finally:
        db.close()

# create exception handling for 400 
def raise_bad_request(msg):
    raise HTTPException(status_code=400, detail=msg)

# not found exception for handling 404 
def raise_not_found(req):
    message = f"URL '{req.url}' does not exist"
    raise HTTPException(status_code=400, detail=message)

#
# path op dectorator to associate root path for GET requests
# fastapi listens to root path & tells all incoming get req to go to read_root() fn
# uses uvicorn as server
# GET METHOD
#
@app.get("/")
def read_root():
    # return string when request to root path is sent
    return 'This is url shortner'

# GET method for url_key
@app.get("/{url_key}")
def forward_to_target_url(
        url_key: str,
        req: Request,
        db: Session = Depends(get_db)
    ):
    db_url = (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )
    # 
    # @previous
    # if db_url:
    # new: using assignment expression := walrus operator (assign var in middle of an expression)
    # if db__url is db entry, then redirect to target_url (longer url)
    # 
    if db_url := crud_ops.get_db_url_by_key(db=db, url_key=url_key):
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)




# POST METHOD
@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    try:
        if not validators.url(url.target_url):
            raise_bad_request(msg="### The URL is not valid")
        
        ''' deprecated method, using keygen mod in crud_ops module
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "".join(secrets.choice(chars) for _ in range(5))
        secret_key = "".join(secrets.choice(chars) for _ in range(8))
        # crud_ops module creates db_url with fn
        db_url = models.URL(
            target_url = url.target_url, key=key, secret_key=secret_key
        )
        '''
        # create db_url using crud_ops fn, get db object back
        db_url = crud_ops.create_db_url(db=db, url=url)
        '''
        #deprecated
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        db_url.url = key
        db_url.admin_url = secret_key
        '''
        # add key to request/resp
        db_url.url = db_url.key
        db_url.admin_url = db_url.secret_key

        return db_url
    except:
        return f'### Error: create_url fn error in post request...'
    # return f'TODO: Create DB Entry for: {url.target_url}'

# @local-testing
# db=SessionLocal()
# print(db.query(models.URL).all())