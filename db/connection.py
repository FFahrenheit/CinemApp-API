import mysql.connector

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                user='cinemapp_admin',
                password='Inception2001',
                database='cinemapp'
            )
            self.cursor = self.connection.cursor()
        except:
            print('Cannot connect!')

    def add_user(self, correo, contraseña):
        try:
            
            query = "INSERT INTO usuario(correo,contraseña) " \
                "VALUES (%s,%s)"
                
            self.cursor.execute(query, (correo,contraseña))
            self.connection.commit()

            return self.cursor.rowcount > 0
        except:
            return False

    def get_users(self):

        query = 'SELECT * FROM usuario'

        self.cursor.execute(query)

        users = []
        for row in self.cursor.fetchall():
            user = {
                'id': row[0],
                'correo': row[1],
                'contraseña': row[2]
            }
            users.append(user)

        return users

    def __del__(self):
        self.connection.close()