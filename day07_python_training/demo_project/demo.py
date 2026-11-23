from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

# basic syntax of decorator
# @decorator_name
# def func_name()
# pass

def my_decorator(func):
    def wrapper():
        print("Before function execution")
    return wrapper

@my_decorator
def greet():
    print("Hello Cloud trainees!")