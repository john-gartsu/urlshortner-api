from fastapi import FastAPI

# instantiate FastAPI class
app = FastAPI()


# path op dectorator to associate root path for GET requests
@app.get("/")
def read_root():
    return 'This is url shortner'

