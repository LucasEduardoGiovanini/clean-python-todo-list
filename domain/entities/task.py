import uuid
from domain.exception.custom_exception import TodoListError


class Task:
    def __init__(self, name, description, completed, priority):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.completed = completed
        self.priority = priority  # informa a prioridade da task, exemplo: uma task com priridade 1 é mais importante que uma de prioridade 2

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def description(self):
        return self._description

    # setter
    @description.setter
    def description(self, value: str):
        self._description = value

    # getter
    @property
    def completed(self):
        return self._completed

    # setter
    @completed.setter
    def completed(self, value: bool):
        if isinstance(value, bool):
            self._completed = value
        else:
            raise TodoListError("Type invalid", 22, "the object type is not Boolean")

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value: int):
        if isinstance(value, int):
            self._priority = value
        else:
            raise TodoListError("Type invalid", 36, "the object type is not Integer")

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
