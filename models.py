from datetime import datetime


class Todo():
    # id = 1
    def __init__(self, title, due_date, completed=False):
        # self.id = Todo.id
        self.title = title
        self.creation_date = str(datetime.now())
        self.last_updated_date = str(datetime.now())
        self.due_date = due_date
        self.completed = (True if completed and completed.lower()
                          == 'true' else False)
        self.completion_date = (str(datetime.now()) if self.completed
                                is True else None)
        # Todo.id += 1

    def toJSON(self):
        return self.__dict__
