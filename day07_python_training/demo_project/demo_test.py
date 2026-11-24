# import modules from libraries
from datetime import date
from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    id: int
    name: str
    hire_date: date

print(Employee(id='1', name="Carla Rivera", hire_date='2026-11-10'))

# use ValidationError when there is a potential failure in input given
try:
    Employee(id="two", name="Josie Fouda", hire_date='2026-11-10')
except ValidationError as exc:
    if (exc.error_count() > 0):
        print(exc.errors()[0]["msg"])

## Unit testing (very important for devops!!)
import pytest
from fastapi.testclient import TestClient
# from day07_python_training.demo_project.demo_app import app # import the app we create in demo_app.py
from demo_app import app # import the app from demo_app.py

client = TestClient(app) # create a new TestClient attached to our app

def test_list_servers_filters_by_env(): # write a test method to test getting servers list with GET call
    resp = client.get("/servers", params={"env":"prod"}) # client.get will make GET request to app and will pass necessary parameters in params as key-value
    assert resp.status_code == 200
    assert [s["name"] for s in resp.json()] == ["Web-03"]

@pytest.mark.parametrize(("server_id", "expected"), [(1,200), (2, 200), (99, 404)]) # pytest.mark.parameterize will let you make the call with a list of parameters to check various options
# the set up is that you say first what each param is ("server_id", "expected") and then you give the list of the params you want to run it wit [(1, 200), (2, 200), (99, 404)] and it will run through each set of params
def test_get_server_status(server_id, expected):
    assert client.get(f"/servers/{server_id}").status_code == expected

# To install dependencies:
# python -m pip install fastapi pytest httpx

# To run the test file:
# python -m pytest demo_01.py

# To run the test file with verbose output:
# python -m pytest demo_01.py -v -s