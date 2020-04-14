from domain.entities.task import Task
class TodoList:
    def __init__(self,name):
        self.name = name
        self.tasks = list()

    def addTask(self,task:Task):
        return self.tasks.append(task)

    def removeTask(self,task:Task):
        return self.tasks.remove(task)


    def __str__(self):
        return "nome lista: " + self.name + " tarefas: " + str(self.tasks)


    def orderTasks(self,task_to_be_relocated:Task,task_that_give_position:Task):

        self.removeTask(task_to_be_relocated)
        index_realocation = self.tasks.index(task_that_give_position)
        self.tasks.insert(index_realocation,task_to_be_relocated)
        return self.tasks

