import mysql.connector
import hashlib

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

    def crear_usuario(self, correo, contraseña):
        if self.existe_usuario(correo):
            return False
        else:
            h = hashlib.new('sha256', bytes(contraseña, 'utf-8'))
            h = h.hexdigest()
            query = "INSERT INTO usuario(correo, contraseña) VALUES (%s, %s)"
            self.cursor.execute(query, (correo, h))
            self.connection.commit()

            return True

    def existe_usuario(self, correo):
        query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
        self.cursor.execute(query, (correo,))

        return self.cursor.fetchone()[0] == 1

    def get_usuarios(self):
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