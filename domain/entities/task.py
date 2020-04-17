class Task:
    def __init__(self, name, description, completed, priority):
        self.name = name
        self.description = description
        self.completed = completed
        self.priority = priority  # informa a prioridade da task, exemplo: uma task com priridade 1 é mais importante que uma de prioridade 2

    def completeTask(self):
        self.completed = True
        return self.completed

    def undoTask(self):
        self.completed = False
        return self.completed

    def __repr__(self):
        return f"<Task {self.name}: {self.completed}>"
