import time


class Todo():
    id = 1

    def __init__(self, title, due_date, completed=False):
        self.id = Todo.id
        self.title = title
        self.creation_date = time.time()
        self.last_updated_date = time.time()
        self.due_date = due_date
        self.completed = (True if completed and completed.lower()
                          == 'true' else False)
        self.completion_date = time.time() if self.completed is True else None
        Todo.id += 1

    def toJSON(self):
        return self.__dict__
