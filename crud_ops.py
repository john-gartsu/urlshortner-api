'''
CRUD ops for DB items
'''

from sqlalchemy.orm import Session
# custom modules
import keygen
import models
import schemas


# create db_url using unique key (added logic in current sprint)
def create_db_url(db: Session, url: schemas.URLBase) -> models.URL:
    # try:
    key = keygen.create_unique_random_key(db)
    secret_key = f"{key}_{keygen.create_random_key(length=12)}"
    print(secret_key)
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
    # except:
    #     return f'### Error occured in function create_db_url() call ###'

# function to get db_url by the key
# returns None or a db entry with a provded key
def get_db_url_by_key(db: Session, url_key: str) -> models.URL:
    return (
        # cause of error 
        # db.query(models.URl)
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )


