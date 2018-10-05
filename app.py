"""
This is a RESTful API for a todos application.
"""
# standard library imports
import logging
import logging.handlers
from datetime import datetime
# related third-party imports
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
# local application import(s)
from models import Todo

# setting up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
)
file_handler = logging.handlers.RotatingFileHandler(
    'todos.log', maxBytes=5*1024*1024, backupCount=2
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# setting up flask and api
app = Flask(__name__)
api = Api(app)

# dictionary that stores data
TODOS = {
    "1": {
        "title": "collect pollen from flowers",
        "creation_date": "2018-10-03 12:47:46.264942",
        "last_updated_date": "2018-10-03 12:47:46.264942",
        "due_date": None,
        "completed": False,
        "completion_date": None
    },
    "2": {
        "title": "buzzbuzzbuzz",
        "creation_date": "2018-10-02 10:31:29.264935",
        "last_updated_date": "2018-10-02 10:31:29.264935",
        "due_date": "soon",
        "completed": False,
        "completion_date": None
    },
}


def abort_if_no_todo(todo_id):
    """
    Aborts mission if given a todo_id that does not exist.
    """
    if todo_id not in TODOS:
        abort(404, message="Todo with id of {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('due_date')
parser.add_argument('completed')


class TodoListItem(Resource):
    """
    Handles GET, DELETE, and PUT requests to '/todos/<todo_id>' endpoint.
    Given a request, returns the response as a JSON object.
    """

    def get(self, todo_id):
        abort_if_no_todo(todo_id)
        logger.info({'message': 'Single Todo: {}'.format(TODOS[todo_id])})
        return {'message': 'Single Todo: {}'.format(TODOS[todo_id])}

    def delete(self, todo_id):
        abort_if_no_todo(todo_id)
        del TODOS[todo_id]
        logger.info({'message': 'Todo deleted with id: {}'.format(todo_id)})
        return {'message': 'Todo deleted with id: {}'.format(todo_id)}, 204

    def put(self, todo_id):
        args = parser.parse_args()
        if args['completed']:
            TODOS[todo_id].update(
                {
                    'completed': (
                        True if args['completed'].lower()
                        == 'true' else False
                    ),
                    'completion_date': (
                        str(datetime.now()) if args['completed'].lower(
                        ) == 'true' else None
                    )
                }
            )
        if args['due_date']:
            TODOS[todo_id].update({
                'due_date': args['due_date']
            })
        if args['title']:
            TODOS[todo_id].update({
                'title': args['title']
            })
        TODOS[todo_id].update({'last_updated_date': str(datetime.now())})
        logger.info({'message': 'Todo updated: {}'.format(TODOS[todo_id])})
        return {'message': 'Todo updated: {}'.format(TODOS[todo_id])}, 201


class TodoList(Resource):
    """
    Handles GET and POST requests for '/todos' endpoint.
    Given a request, returns the response as a JSON object.
    """

    def get(self):
        logger.info({'message': TODOS})
        return {'message': TODOS}

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys())) + 1 if TODOS else 1
        todo_id = str(todo_id)
        TODOS[todo_id] = Todo(
            args['title'],
            args['due_date'],
            args['completed']
        ).toJSON()
        logger.info({'message': 'Todo created: {}'.format(TODOS[todo_id])})
        return {'message': 'Todo created: {}'.format(TODOS[todo_id])}, 201


# adding some resources with assgined endpoints to api
api.add_resource(TodoListItem, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos')

if __name__ == "__main__":
    app.run(debug=True)
