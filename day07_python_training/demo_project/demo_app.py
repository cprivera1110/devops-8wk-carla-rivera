from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel


# basic syntax of decorator
# @decorator_name
# def func_name()

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def greet():
    print("Hello Cloud trainees!")

greet()

## Class
# a collection of variables and functions which define the behavior of a new Object

app = FastAPI(title="Demo Cloud App", version="1.0.0")
class Server(BaseModel): # Pydantic model = schema + validation
    id: int
    name: str
    env: str

SERVERS = [Server(id=1,name="Web-01",env="dev"), Server(id=2,name="Web-02",env="dev"), Server(id=3,name="Web-03",env="prod")]

# Root endpoint
@app.get("/")
def home():
    return { "message": "Welcome to the Demo Cloud App!" }

@app.get("/servers", response_model=list[Server]) # using a decorator for the call to the API endpoint for the 'get' call, response model tells you what form the response will take
def list_server(env: Annotated[str | None, Query(description="Filter by env")] = None): # Annotated adds metadata info to endpoint response(?)
    # query parameter: /servers?env=prod
    return [s for s in SERVERS if env is None or s.env == env] # list comprehension to filter the list for only the servers with 'prod' env

@app.get("/servers/{server_id}", response_model=Server)
def get_server(server_id:int): # path parameter, converted to int
    for s in SERVERS:
        if (s.id == server_id):
            return s
    raise HTTPException(status_code=404, detail="Server not found")

# To install dependencies:
# python -m pip install fastapi uvicorn

# To start the app:
# python3 -m uvicorn demo:app --reload

# To view dashboard style info about API:
# http://127.0.0.1:8000/docs# <-- add /docs# at the end for Swagger UI

# To make calls for debugging in a separate terminal:
# curl http://127.0.0.1:8000/servers
# curl http://127.0.0.1:8000/servers?env=prod
# curl http://127.0.0.1:8000/servers/{id}