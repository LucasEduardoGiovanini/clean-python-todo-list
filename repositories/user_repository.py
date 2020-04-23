import pymysql


class UserRepository:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='lucasgiovanini',
                                          db='dbTodoList',
                                          cursorclass=pymysql.cursors.DictCursor)

    def insert_user(self, email: str, password: str):
        cursor = self.connection.cursor()
        arguments = (email, password)
        cursor.execute("INSERT INTO tbUsuario (email,senha) VALUES(%s,%s)", arguments)
        self.connection.commit()
        cursor.execute("SELECT email FROM tbUsuario where email=%s", arguments[0])
        datas = cursor.fetchone()
        return datas

    def get_code_from_user_list(self, email: str):
        cursor = self.connection.cursor()
        arguments = (email,)
        cursor.execute("SELECT cod_todolist FROM tbTodoList WHERE email = %s", arguments)
        result = cursor.fetchall()
        return result

    def recover_user_list(self, list_id: str):
        cursor = self.connection.cursor()
        arguments = (list_id,)
        cursor.execute("SELECT * FROM tbTask WHERE cod_todolist = %s", arguments)
        return cursor.fetchall()