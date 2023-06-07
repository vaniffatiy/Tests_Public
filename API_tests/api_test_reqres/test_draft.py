import requests
from conftest import *

def test_get_list_of_users():
    response = requests.get(url+path_to_create)
    assert response.status_code == 200

def test_create_new_user(put_payload):
    response = requests.post(url+path_to_create, data=put_payload)
    assert response.status_code == 201

def test_update_user(put_payload):
    response = requests.put(url+path_to_put, data=put_payload)
    assert response.status_code == 200

def test_delete_user():
    response = requests.delete(url+path_to_delete)
    assert response.status_code == 204