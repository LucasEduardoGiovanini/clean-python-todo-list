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
        cursor.execute("INSERT INTO tbTodoList(cod_todolist, email, list_name) VALUES (%s, %s, %s)", arguments)
        self.connection.commit()
        cursor.execute("SELECT * FROM tbTodoList WHERE cod_todolist = %s", arguments[0])
        return cursor.fetchone()

    def get_the_next_free_position(self, id_list: str):# pego a maior posição da fila
        cursor = self.connection.cursor()
        arguments = (id_list,)
        cursor.execute("SELECT queue_position FROM tbTask WHERE queue_position = (SELECT MAX (queue_position)from tbTask) and cod_todolist = %s", arguments)
        result = cursor.fetchone()
        return result if result is not None else False

    def create_task(self, id_task: str, id_list: str, name: str, description: str, completed: bool, priority: int, queue_position: int):
        cursor = self.connection.cursor()
        arguments = (id_task, id_list, name, description, completed, priority, queue_position)
        cursor.execute("INSERT INTO tbTask(cod_task,cod_todolist,name_task,descripton,completed,priority,queue_position) VALUES (%s, %s, %s,%s,%s,%s,%s)", arguments)
        self.connection.commit()
        cursor.execute("SELECT * FROM tbTask WHERE cod_task = %s", arguments[0])
        return cursor.fetchone()
