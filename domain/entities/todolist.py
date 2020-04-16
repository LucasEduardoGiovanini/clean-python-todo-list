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


    def orderTasks(self,task_to_be_relocated:Task,position: int):
        try:
            self.removeTask(task_to_be_relocated)
            self.tasks.insert(position,task_to_be_relocated)
        except IndexError:
            return "posição incorreta"
        except ValueError:
            return "a tarefa não existe na lista"
        else:
            return self.tasks