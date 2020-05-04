from domain.entities.task import Task
from domain.exception.custom_exception import TodoListError
import operator


class TodoList:
    def __init__(self, todo_name, email_creator):
        self.todo_name = todo_name
        self.email_creator = email_creator

    def create_task(self, todolist_id, name: str, description: str, completed: bool, priority: int):
        task_created = Task(todolist_id, name, description, completed, priority)
        self.add_task(task_created)
        return task_created

    def add_task(self, task: Task):
        self.tasks.append(task)
        return self.tasks

    def undo_task(self, task: Task):
            return task.undo()

    def complete_task(self, task: Task):
            return task.complete()

    def remove_task(self, task: Task):
        del task
        return True

    def edit_task(self, task: Task, name=None, description=None, completed=None, priority=None):
        return task.edit(name, description, completed, priority)

    def edit_list_name(self, name=None):
        self.todo_name = name or self.todo_name
        return self.todo_name

    def __str__(self):
        return "nome lista: " + self.todo_name + " tarefas: " + str(self.tasks)

    def sort_tasks_by_priority(self):
        self.tasks = sorted(self.tasks, key=operator.attrgetter("priority"))
        return self.tasks

    def order_task(self, task_to_be_relocated: Task, position: int):
        self.remove_task(task_to_be_relocated)
        self.tasks.insert(position, task_to_be_relocated)
        return self.tasks
