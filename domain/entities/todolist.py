from domain.entities.task import Task
from domain.exception.custom_exception import TodoListError
import operator
import uuid


class TodoList:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.tasks = list()

    def create_task(self, name: str, description: str, completed: bool, priority: int):

        if isinstance(name, str) and isinstance(description, str) and isinstance(completed, bool) and isinstance(priority, int):
            task_created = Task(name, description, completed, priority)
            self.add_task(task_created)
            return task_created
        else:
            message_error = "Expected: str, str, bool, int / Received: ", type(name), type(description), type(completed), type(priority)
            raise TodoListError("Some parameter(s) informed are receiving inappropriate types", 13, message_error)

    def add_task(self, task: Task):
        self.tasks.append(task)
        return self.tasks

    def undo_task(self, task: Task):
        try:
            self.tasks[self.tasks.index(task)].undo()
        except ValueError as ve:
            raise TodoListError(ve, 22, "undo a task that does not exist in this list")
        except IndexError as ie:
            raise TodoListError(ie, 22, "the informed index is greater than the list")
        else:
            return task

    def complete_task(self, task: Task):
        try:
            self.tasks[self.tasks.index(task)].complete()
        except ValueError as ve:
            raise TodoListError(ve, 30, "completing a task that does not exist in this list")
        except IndexError as ie:
            raise TodoListError(ie, 30, "the informed index is greater than the list")
        else:
            return task

    def remove_task(self, task: Task):
        try:
            self.tasks.remove(task)
        except ValueError as ve:
            raise TodoListError(ve, 38, "removing a task that does not exist in this list")
        except IndexError as ie:
            raise TodoListError(ie, 38, "the informed index is greater than the list")
        else:
            return True

    def edit_task(self, task: Task, name=None, description=None, completed=None, priority=None):
        try:
            self.tasks[self.tasks.index(task)].edit(name, description, completed, priority)
        except ValueError as ve:
            raise TodoListError(ve, 46, "update a task that does not exist in this list")
        except IndexError as ie:
            raise TodoListError(ie, 46, "the informed index is greater than the list")
        else:
            return task

    def edit_list_name(self, name=None):
        self.name = name or self.name
        return self.name

    def __str__(self):
        return "nome lista: " + self.name + " tarefas: " + str(self.tasks)

    def sort_tasks_by_priority(self):
        self.tasks = sorted(self.tasks, key=operator.attrgetter("priority"))
        return self.tasks

    def order_task(self, task_to_be_relocated: Task, position: int):
        self.remove_task(task_to_be_relocated)
        self.tasks.insert(position, task_to_be_relocated)
        return self.tasks
