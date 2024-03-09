# Import FastAPI
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a path operation for the root ("/")
@app.get("/")
async def read_root():
    # Return a simple JSON response
    return {"Hello": "World"}
