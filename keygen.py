'''
Generate random secret key for short url
'''
from sqlalchemy.orm import Session
import secrets
import string

# custom modules
import crud_ops

def create_random_key(length: int = 5) -> str:
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

# function to create unique key
# while loop checks to see if key already exists in ur db, ensuring short url exists once
def create_unique_random_key(db: Session) -> str:
    key = create_random_key()
    try:
        while crud_ops.get_db_url_by_key(db, key):
            key = create_random_key()
        return key
    except:
        return f'### ERROR in create_unique_random_key() fn call'

# test to see if function worked
'''
randomKey = create_random_key()
print(randomKey)
'''