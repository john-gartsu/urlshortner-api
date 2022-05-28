'''
Generate random secret key for short url
'''

import secrets
import string

def create_random_key(length: int = 5) -> str:
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

# test to see if function worked
'''
randomKey = create_random_key()
print(randomKey)
'''