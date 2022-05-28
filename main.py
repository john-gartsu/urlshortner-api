import secrets
from fastapi import Depends, FastAPI, HTTPException
import validators
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
# from . import schemas, models
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
@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    try:
        if not validators.url(url.target_url):
            raise_bad_request(msg="### URL not valid")
        
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "".join(secrets.choice(chars) for _ in range(5))
        secret_key = "".join(secrets.choice(chars) for _ in range(8))
        db_url = models.URL(
            target_url = url.target_url, key=key, secret_key=secret_key
        )
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        db_url.url = key
        db_url.admin_url = secret_key

        return db_url
    except:
        return f'### Error: create_url fn error in post request...'
    # return f'TODO: Create DB Entry for: {url.target_url}'
