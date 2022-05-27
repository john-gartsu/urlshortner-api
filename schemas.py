'''
Schema - what api expects as request body
        - what client can expect in resp body

implement type hinting to verify request & resp match data types defined
'''

from pydantic import BaseModel

# create pydantic base models for api req && response
# Basemodel defines URLBase class 
# URLBase clas has target_url str to store the url that ur shortened url fwds to
class URLBase(BaseModel):
    target_url: str

# 
# URL class inherit target_url string from URLBase
# URL class
#    is_active is used to deactivate shortened urls
#    clicks stores how many times short url clicked on
# 
class URL(URLBase):
    is_active: bool
    clicks: int
    # tells its working with ORM to work with db with OOP approach
    class Config:
        orm_mode = True

# 
# enhance URL by adding 2 strings
# allows u to store data in ur api w/o storing it in your db
# 
class URLInfo(URL):
    url: str
    admin_url: str