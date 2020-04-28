import pymysql


class TodoListRepository:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='lucasgiovanini',
                                          db='dbTodoList',
                                          cursorclass=pymysql.cursors.DictCursor)

    def create_todo_list(self, email: str, id_code: str, list_name: str):
        cursor = self.connection.cursor()
        arguments = (id_code, email, list_name)
        cursor.execute("INSERT INTO tbTodoList(todolist_id, email, todo_name) VALUES (%s, %s, %s)", arguments)
        self.connection.commit()
        cursor.execute("SELECT * FROM tbTodoList WHERE todolist_id = %s", arguments[0])
        return cursor.fetchone()

    def get_the_next_free_position(self, id_list: str):# pego a maior posição da fila
        cursor = self.connection.cursor()
        arguments = (id_list,)
        cursor.execute("SELECT max(queue_position) FROM tbTask WHERE todolist_id = %s", arguments)
        result = cursor.fetchone()
        return result['max(queue_position)']+1 if result['max(queue_position)'] is not None else 0# se não tiver nenhuma task, retorno a primeira posição disponível.

    def create_task(self, id_task: str, id_list: str, name: str, description: str, completed: bool, priority: int, queue_position: int):
        cursor = self.connection.cursor()
        arguments = (id_task, id_list, name, description, completed, priority, queue_position)
        cursor.execute("INSERT INTO tbTask(task_id,todolist_id,task_name,descripton,completed,priority,queue_position) VALUES (%s, %s, %s,%s,%s,%s,%s)", arguments)
        self.connection.commit()
        cursor.execute("SELECT * FROM tbTask WHERE task_id = %s", arguments[0])
        return cursor.fetchone()
