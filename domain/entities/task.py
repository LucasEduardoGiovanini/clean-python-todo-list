class Task:
    def __init__ (self,name,description,stats,priority):
        self.name = name
        self.description = description
        self.stats = stats
        self.priority = priority #informa a prioridade da task, exemplo: uma task com priridade 1 é mais importante que uma de prioridade 2


    def completeTask(self): #caso queira alterar o nome
        self.stats = True
        return self.stats

    def undoTask(self):
        self.stats = False
        return self.stats

    def getTask(self,task):
        return " name: "+task.name+"\n description: "+task.description+"\n stats "+str(task.stats)+"\n priority level: "+task.priority+"\n\n"
