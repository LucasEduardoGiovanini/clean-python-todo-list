from domain.exception.custom_exception import TodoListError


class Task:
    def __init__(self,todolist_id, task_name, description, completed, priority):
        self.todolist_id = todolist_id
        self.task_name = task_name
        self.description = description
        self.completed = completed
        self.priority = priority  # informa a prioridade da task, exemplo: uma task com priridade 1 é mais importante que uma de prioridade 2

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
        self.task_name = name or self.task_name
        self.description = description or self.description
        self.completed = completed or self.completed
        self.priority = priority or self.priority
        return self

    def __repr__(self):
        return f"<Task {self.task_name}: {self.completed}>"
