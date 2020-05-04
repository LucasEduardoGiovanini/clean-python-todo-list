import pymysql
from domain.entities.task import Task
from domain.entities.todolist import TodoList


class TodoListRepository:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='lucasgiovanini',
                                          db='dbTodoList',
                                          cursorclass=pymysql.cursors.DictCursor)

    def create_todo_list(self, email: str, list_name: str):
        cursor = self.connection.cursor()
        arguments = (email, list_name)
        cursor.execute("INSERT INTO tbTodoList(email, todo_name) VALUES (%s, %s)", arguments)
        self.connection.commit()
        cursor.execute("SELECT * FROM tbTodoList WHERE email = %s AND todo_name = %s", arguments)
        result_dictionary = cursor.fetchone()
        return TodoList(result_dictionary['todo_name'], result_dictionary['email'])

    def get_the_next_free_position(self, id_list: str):# pego a maior posição da fila
        cursor = self.connection.cursor()
        arguments = (id_list,)
        cursor.execute("SELECT max(queue_position) FROM tbTask WHERE todolist_id = %s", arguments)
        result = cursor.fetchone()
        return result['max(queue_position)']+1 if result['max(queue_position)'] is not None else 0# se não tiver nenhuma task, retorno a primeira posição disponível.

    def create_task(self, id_list: str, name: str, description: str, completed: bool, priority: int):
        cursor = self.connection.cursor()
        queue_position = self.get_the_next_free_position(id_list)
        arguments = (id_list, name, description, completed, priority, queue_position)
        cursor.execute("INSERT INTO tbTask(todolist_id,task_name,descripton,completed,priority,queue_position) VALUES (%s, %s,%s,%s,%s,%s)", arguments)
        self.connection.commit()
        cursor.execute("SELECT * FROM tbTask WHERE todolist_id = %s AND task_name = %s AND descripton = %s AND completed = %s AND priority = %s AND queue_position = %s", arguments)
        result_dictionary = cursor.fetchone()
        return Task(result_dictionary['todolist_id'], result_dictionary['task_name'], result_dictionary['descripton'], bool(result_dictionary['completed']), int(result_dictionary['priority']))

    def recover_list_id_by_namelist_and_email(self, name_list: str, email: str):
        cursor = self.connection.cursor()
        arguments = (name_list, email)
        cursor.execute("SELECT todolist_id FROM tbTodoList WHERE todo_name = %s AND email = %s ",arguments)
        result = cursor.fetchone()
        return result if result is not None else False

    def get_all_a_user_list_with_tasks(self, email: str):
        cursor = self.connection.cursor()
        all_todo_lists_user = []
        arguments = (email,)
        cursor.execute("SELECT * FROM tbTodoList WHERE email = %s", arguments)
        all_todolists = cursor.fetchall()
        for todo_list in all_todolists:# percorro todas as listas
            recovered_list = TodoList(todo_list['todo_name'], todo_list['email']) #crio o objeto lista na aplicação
            tasks = self.recover_all_tasks_from_list(todo_list['todolist_id']) #recupero todas as tasks dessa lista
            one_todo_list = [recovered_list, tasks]
            all_todo_lists_user.append(one_todo_list) #faço um append de uma tupla, contendo a lista e suas tarefas
        return all_todo_lists_user

    def recover_all_tasks_from_list(self, list_id: str):
        list_of_tasks = []
        cursor = self.connection.cursor()
        arguments = (list_id,)
        cursor.execute("SELECT * FROM tbTask WHERE todolist_id = %s", arguments)
        tasks = cursor.fetchall()
        for task in tasks:
            list_of_tasks.append(Task(task['todolist_id'], task['task_name'], task['descripton'], bool(task['completed']), int(task['priority'])))
        return list_of_tasks

    def reinsert_modified_task_into_database(self, task: Task): # essa função será chamada ao final de cada teste para reinserir as alterações no banco
        cursor = self.connection.cursor()
        arguments = (task.task_name, task.description, task.completed, task.priority, task.todolist_id)
        cursor.execute("UPDATE tbTask SET task_name = %s, descripton = %s, completed = %s, priority = %s WHERE todolist_id = %s", arguments)
        self.connection.commit()
        cursor.execute("SELECT * FROM tbTask WHERE task_name = %s AND descripton = %s AND completed = %s AND priority = %s AND todolist_id = %s", arguments)
        return cursor.fetchone()