class TodoList:
    def __init__(self,name):
        self.name = name
        self.tasks = list(None)

    def addTask(self,task:list):
        self.tasks.append(task)

    def removeTask(self,task:str):
        self.tasks.remove(task)

    def getList(self):
        return " list name: "+self.name+"\n tasks: \n"+self.tasks

    def orderTasks(self,order_list:list):
        cloned_list = self.tasks.copy()
        for task in range(0,len(self.tasks)):
            temporary_armazenation_variable = cloned_list[task]
            cloned_list[task] = cloned_list[order_list[task]]
            cloned_list[order_list[task]] = temporary_armazenation_variable
        self.tasks = cloned_list
        return self.tasks
#cria lista
lista1=TodoList("tarefas do dia")

#cria tarefas
tarefa1 = Task("cozinhar","todo dia as 12:00 eu faço almoço",False)
tarefa2 = Task("trabalhar","hoje eu preciso programar 3 classes",False)
tarefa3 = Task("ir ao mercado","comprar batata  e frango",False)

#adiciona tarefas
lista1.addTask(tarefa1,tarefa2,tarefa3)
print(lista1.getList())


print("--------------")
print("--------------")
#completa 1 tarefa
tarefa1.completeTask()
print(lista1.getList())

print("--------------")
print("--------------")
#desfaz a tarefa completada
tarefa1.undoTask()
print(lista1.getList())

print("--------------")
print("--------------")
#ordena a lista de acordo com o desejo do usuário
lista_ordenacao = list(2,1,0)
lista1.orderTasks(lista_ordenacao)
print(lista1.getList())

print("--------------")
print("--------------")
#removo 1 task da lista
lista1.removeTask(tarefa1)
print(lista1.getList())

