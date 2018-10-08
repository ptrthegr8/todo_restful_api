import unittest
import copy
import json
from app import app, abort_if_no_todo, TODOS


class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_abort(self):
        self.assertEqual(abort_if_no_todo("1"), None)
        self.assertEqual(abort_if_no_todo("2"), None)

    def test_get_list(self):
        response = self.app.get('http://localhost:5000/todos')
        dict_res = json.loads(response.data.decode('utf-8'))["message"]
        self.assertEqual(dict_res, TODOS)

    def test_get_list_item(self):
        response = self.app.get('http://localhost:5000/todos/1')
        dict_res = json.loads(response.data.decode('utf-8'))["message"]
        self.assertEqual(dict_res, "Single Todo: {}".format(TODOS.get("1")))

    def test_post_list_item(self):
        payload = {'title': 'test', 'due_date': '10/31/18', 'completed': False}
        response = self.app.post('http://localhost:5000/todos', data=payload)
        dict_res = json.loads(response.data.decode('utf-8'))["message"]
        self.assertEqual(dict_res, 'Todo created: {}'.format(TODOS.get("3")))

    def test_put_list_item(self):
        payload = {'title': 'updated_title', 'due_date': '10/20/20',
                   'completed': False}
        response = self.app.put('http://localhost:5000/todos/2', data=payload)
        dict_res = json.loads(response.data.decode('utf-8'))["message"]
        self.assertEqual(dict_res, 'Todo updated: {}'.format(TODOS["2"]))


if __name__ == '__main__':
    unittest.main()
