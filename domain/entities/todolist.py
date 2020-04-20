from domain.entities.task import Task
from domain.exception.custom_exception import todoListError
import operator


class TodoList:
    def __init__(self, name):
        self.name = name
        self.tasks = list()

    def create_task(self, name: str, description: str, completed: bool, priority: int):
        task_created = Task(name, description, completed, priority)
        self.add_task(task_created)
        return task_created

    def add_task(self, task: Task):
        self.tasks.append(task)
        return self.tasks

    def undo_task(self, task: Task):
        try:
            self.tasks[self.tasks.index(task)].undo()
        except ValueError as ve:
            raise todoListError(ve, 14, "undo a task that does not exist in this list")
        else:
            return task

    def complete_task(self, task: Task):
        try:
            self.tasks[self.tasks.index(task)].complete()
        except ValueError as ve:
            raise todoListError(ve, 14, "completing a task that does not exist in this list")
        else:
            return task

    def remove_task(self, task: Task):
        try:
            self.tasks.remove(task)
        except ValueError as ve:
            raise todoListError(ve, 13, "removing a task that does not exist in this list")
        else:
            return True

    def edit_task(self, task: Task, name=None, description=None, completed=None, priority=None):
        try:
            self.tasks[self.tasks.index(task)].edit(name, description, completed, priority)
        except ValueError as ve:
            raise todoListError(ve, 24, "update a task that does not exist in this list")
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
