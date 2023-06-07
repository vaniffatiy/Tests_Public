import pytest

@pytest.fixture
def create_payload():
    data = {
        "name": "Paulo Oliveira",
        "movies": ["I Love You Man", "Role Models"]
    }
    return data

@pytest.fixture
def put_payload():
    data = {
        "name": "Paulo Updated"
    }
    return data


url = "https://reqres.in"
path_to_get = "/api/users/2"
path_to_create = "/api/users"
path_to_put = "/api/users/2"
path_to_delete = "/api/users/2"


