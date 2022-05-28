### URL SHORTNER API 

Using Python and FastAPI to build URL Shortner API

1.) ENV Set up
    >>>> Added .env_sample file for 12-factor app method, this is only      sample for how to make .env that will be gitignored

    >>>> Please add .env to your .gitignore file
    >>> activate venv: source venv/bin/activate  (mac/linux)

2.) Set up url shortner
    >>>> run server with cmd: uvicorn url_shortener_app.main:app --reload

3. Clean code

4. Manage && Save urls in db sql lite
   a. create admin endpoint to view info about url accessed only by user with secret key

   b. update visitor count

### debug journey
1. Validation Error was actually ln 32 in crud ops typo- AttributeError: module 'models' has no attribute 'URl' - l not L upper