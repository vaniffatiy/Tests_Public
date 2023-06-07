import pytest

create_payload = {
  "content": "string1",
  "user_id": "string2",
  "task_id": "string3",
  "is_done": False
}

put_payload = {
  "content": "string7",
  "user_id": "string5",
  "task_id": "string4",
  "is_done": True
}

@pytest.fixture
def expected_headers():
  value = ('159', 'keep-alive', 'Miss from cloudfront')
  return value

url = "https://todo.pixegami.io/"
path_to_create = "/create-task"
path_to_get = "/get-task/"
path_to_put = "/update-task/"
path_to_delete = "/delete-task/"


