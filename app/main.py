# Import the FastAPI class from the fastapi module
from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()

# Define a route for the root URL ("/") using the GET HTTP method
@app.get("/")
def read_root():
    # Return a JSON response with a message key
    return {"message": "Hello from FastAPI and Docker!"}

