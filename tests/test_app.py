import unittest
import json
from app import app, TODOS


class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_test(self):
        self.assertEqual(type(TODOS), type(dict()))

    def test_get_initial_dict(self):
        response = self.app.get('http://localhost:5000/todos')
        dict_res = json.loads(response.data.decode('utf-8'))["message"]
        self.assertEqual(dict_res, TODOS)

    def test_get_list_item(self):
        response = self.app.get('http://localhost:5000/todos/1')
        dict_res = json.loads(response.data.decode('utf-8'))["message"]
        self.assertEqual(dict_res, "Single Todo: {}".format(TODOS.get("1")))


if __name__ == '__main__':
    unittest.main()
