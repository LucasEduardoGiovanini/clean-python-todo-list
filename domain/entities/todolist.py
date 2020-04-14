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


    def orderTasks(self,order_list:list):
        cloned_list = self.tasks.copy()
        for task in range(0,len(self.tasks)-1):
            temporary_armazenation_variable = cloned_list[task]
            cloned_list[task] = cloned_list[order_list[task]]
            cloned_list[order_list[task]] = temporary_armazenation_variable
        self.tasks = cloned_list
        cloned_list = list()
        return self.tasks

