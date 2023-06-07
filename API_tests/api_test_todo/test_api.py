# from api_test_todo.conftest import set_create_payload
from API_tests_local.api_test_todo.page_api import *


class TestModel(PageModel):

    def test_get(self):
        response = self.get_response()
        assert response.status_code == 200
        assert response.json()["is_done"] is False
        assert len(response.json()) > 0

    def test_create(self, expected_headers):
        response = self.post_response()
        actual_headers = (
            response.headers['Content-Length'],
            response.headers['Connection'],
            response.headers['X-Cache']
        )
        assert response.status_code == 200
        assert actual_headers == expected_headers

    def test_put(self):
        response = self.put_response()
        assert response.json()["updated_task_id"] == "string4"
        assert response.status_code == 200

    def test_delete(self):
        response = self.delete_response()
        assert response.status_code == 200
