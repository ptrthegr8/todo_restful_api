from flask import Flask
from flask_restful import reqparse, Api, Resource
from models import Todo

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {
        'task': 'collect pollen from flowers',
        'creation_date': 'now',
        'last_updated_date': 'then',
        'due_date': 'soon',
        'completed': True,
        'completion_date': None
    },
    'todo2': {
        'task': 'buzzbuzzbuzz',
        'creation_date': 'now',
        'last_updated_date': 'then',
        'due_date': 'soon',
        'completed': False,
        'completion_date': None
    },
    'todo3': {
        'task': 'profit with honey!',
        'creation_date': 'now',
        'last_updated_date': 'then',
        'due_date': 'soon',
        'completed': False,
        'completion_date': None
    },
}

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('due_date')
parser.add_argument('completed')


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo{}'.format(todo_id)
        TODOS[todo_id] = Todo(args['title'],
                              args['due_date'],
                              args['completed']
                              ).toJSON()
        return TODOS[todo_id], 201


api.add_resource(TodoList, '/todos')

if __name__ == "__main__":
    app.run(debug=True)
