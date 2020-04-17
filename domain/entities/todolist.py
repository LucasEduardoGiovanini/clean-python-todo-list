from domain.entities.task import Task
from domain.exception.custom_exception import todoListError
class TodoList:
    def __init__(self,name):
        self.name = name
        self.tasks = list()

    def addTask(self,task:Task):
        self.tasks.append(task)
        return self.tasks

    def removeTask(self,task:Task):
        try:
           removed = self.tasks.remove(task)
        except ValueError as ve:
            raise todoListError(ve, 13, "removing a task that does not exist in this list")
        else:
            return True


    def __str__(self):
        return "nome lista: " + self.name + " tarefas: " + str(self.tasks)


    def orderTasks(self,task_to_be_relocated:Task,position: int):
        self.removeTask(task_to_be_relocated)
        self.tasks.insert(position,task_to_be_relocated)
        return self.tasks
