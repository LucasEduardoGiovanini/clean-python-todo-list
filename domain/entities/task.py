class Task:
    def __init__ (self,name,description,stats):
        self.name = name
        self.description = description
        self.stats = stats



    def completeTask(self): #caso queira alterar o nome
        self.stats = True
        return self.stats

    def undoTask(self):
        self.stats = False
        return self.stats

    def getTask(self):
        return " name: "+self.name+"\n description: "+self.description+"\n stats "+self.stats
