'''
CRUD ops for DB items
'''

from sqlalchemy.orm import Session
# custom modules
import keygen
import models
import schemas

def create_db_url(db: Session, url: schemas.URLBase) -> models.URL:
    try:
        key = keygen.create_random_key()
        secret_key = keygen.create_random_key(length=12)
        db_url = models.URL(
            target_url=url.target_url, key=key, secret_key=secret_key
        )
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        return db_url
    except:
        return f'### Error occured in function create_db_url() call ###'
