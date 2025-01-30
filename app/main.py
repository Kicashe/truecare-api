
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI(title="TrueCare API", version="1.0.0")

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to TrueCare!"}

# Define another endpoint
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}