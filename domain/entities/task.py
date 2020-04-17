class Task:
    def __init__(self, name, description, completed, priority):
        self.name = name
        self.description = description
        self.completed = completed
        self.priority = priority  # informa a prioridade da task, exemplo: uma task com priridade 1 é mais importante que uma de prioridade 2

    def complete(self):
        self.completed = True
        return self.completed

    def undo(self):
        self.completed = False
        return self.completed

    def edit(self, name=None, description=None, completed=None, priority=None):
        self.name = name or self.name
        self.description = description or self.description
        self.completed = completed or self.completed
        self.priority = priority or self.priority
        return self

    def __repr__(self):
        return f"<Task {self.name}: {self.completed}>"
