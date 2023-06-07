import requests
from API_tests_local.api_test_todo.conftest import *



class PageModel:
    def __set_task_id(self):
        task_id = requests.put(url+path_to_create, json=create_payload).json()["task"]["task_id"]
        return task_id

    def post_response(self):
        response = requests.put(url+path_to_create, json=create_payload)
        return response

    def get_response(self):
        task_id = str(self.__set_task_id())
        response = requests.get(url+path_to_get+task_id)
        return response


    def put_response(self):
        response = requests.put(url+path_to_put, json=put_payload)
        return response

    def delete_response(self):
        task_id = self.__set_task_id()
        response = requests.delete(url+path_to_delete+task_id)
        return response

