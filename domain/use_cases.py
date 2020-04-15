from .entities.task import Task
from .entities.todolist import TodoList


def Create_list(listname: str):
    if type(listname)== str:
        list1 = TodoList(listname)
        return listname
    return False


def add_task(task_list: TodoList, task: Task):
    task_list.addTask(task)
    return task


def remove_task(task_list: TodoList, task: Task):
    if task in task_list.tasks:
        task_list.removeTask(task)
        return task
    return False


def complete_task(task_list: TodoList, task: Task):
    if task in task_list.tasks:
        task.completeTask()
        return task
    return False


def undo_task(task_list: TodoList, task: Task):
    if task in task_list.tasks:
        task.undoTask()
        return task
    return False


def order_task(task_list: TodoList, task_to_be_relocated: Task, task_that_give_position: Task):
    if task_to_be_relocated in task_list.tasks and task_that_give_position in task_list.tasks:
        task_list.orderTasks(task_to_be_relocated, task_that_give_position)
        return True
    return False
