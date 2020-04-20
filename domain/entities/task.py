import uuid
from domain.exception.custom_exception import TodoListError

class Task:
    def __init__(self, name, description, completed, priority):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.completed = completed
        self.priority = priority  # informa a prioridade da task, exemplo: uma task com priridade 1 é mais importante que uma de prioridade 2

    # getter
    @property
    def completed(self):
        try:
            return self._completed
        except AttributeError as ae:
            raise TodoListError(ae, 16, "the object type is not boolean")

    # setter
    @completed.setter
    def completed(self, value: bool):
        if isinstance(value, bool):
            self._completed = value

    @property
    def priority(self):
        try:
            return self._priority
        except AttributeError as ae:
            raise TodoListError(ae, 31, "the object type is not Integer")

    @priority.setter
    def priority(self, value: int):
        if isinstance(value, int):
            self._priority = value

    def complete(self):
        self.completed = True
        return self.completed

    def undo(self):
        self.completed = False
        return self.completed

    def edit(self, name=None, description=None, completed=None, priority=None):
        self.name = name or self.name
        self.description = description or self.description
        self.completed = completed or self.completed
        self.priority = priority or self.priority
        return self

    def __repr__(self):
        return f"<Task {self.name}: {self.completed}>"
