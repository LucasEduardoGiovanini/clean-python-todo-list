from domain.entities.task import Task
from domain.exception.custom_exception import todoListError
class TodoList:
    def __init__(self,name):
        self.name = name
        self.tasks = list()

    def add_task(self, task:Task):
        self.tasks.append(task)
        return self.tasks

    def remove_task(self, task:Task):
        try:
           removed = self.tasks.remove(task)
        except ValueError as ve:
            raise todoListError(ve, 13, "removing a task that does not exist in this list")
        else:
            return True

    def edit_task(self,task:Task, name=None, description=None, completed=None, priority=None):
        try:
            self.tasks[self.tasks.index(task)].edit(name,description,completed,priority)
        except ValueError as ve:
            raise todoListError(ve,24,"update a task that does not exist in this list")
        else:
            return task

    def edit_list_name(self,name = None):
        self.name = name or self.name
        return self.name

    def __str__(self):
        return "nome lista: " + self.name + " tarefas: " + str(self.tasks)


    def order_task(self, task_to_be_relocated:Task, position: int):
        self.remove_task(task_to_be_relocated)
        self.tasks.insert(position,task_to_be_relocated)
        return self.tasks
