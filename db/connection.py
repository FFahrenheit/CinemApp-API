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

    def iniciar_sesion(self, correo, contraseña):
        h = hashlib.new('sha256', bytes(contraseña, 'utf-8'))
        h = h.hexdigest()
        
        query = 'SELECT id FROM usuario WHERE correo = %s AND contraseña = %s'
        self.cursor.execute(query, (correo, h))
        
        id = self.cursor.fetchone()

        if id:
            return id[0], True
        else:
            return None, False

    def insertar_pelicula(self, pelicula):
        titulo = pelicula['titulo']
        fecha_visto = pelicula['fecha_visto']
        imagen = pelicula['imagen']
        director = pelicula['director']
        año = pelicula['año']
        usuarioId = pelicula['usuarioId']

        query = "INSERT INTO pelicula \
            (titulo, fecha_visto, imagen, director, año, usuarioId) \
            VALUES(%s, %s, %s, %s, %s, %s)"

        self.cursor.execute(query, (titulo, fecha_visto, imagen, director, año, usuarioId))

        self.connection.commit()

        return self.cursor.rowcount

    def get_peliculas(self):
        query = "SELECT id, titulo, imagen, fecha_visto, director, año FROM pelicula"
        
        self.cursor.execute(query)
        peliculas = []

        for row in self.cursor.fetchall():
            pelicula = {
                'id': row[0],
                'titulo': row[1],
                'imagen': row[2],
                'fecha_visto': row[3],
                'director': row[4],
                'año': row[5]
            }
            peliculas.append(pelicula)

        return peliculas

    def get_pelicula(self, id):
        query = "SELECT * FROM pelicula WHERE id = %s"
        
        self.cursor.execute(query, (id,))
        
        row = self.cursor.fetchone()
        pelicula = {}
        
        if row:
            pelicula = {
                'id': row[0],
                'titulo': row[1],
                'fecha_visto': row[2],
                'imagen': row[3],
                'director': row[4],
                'año': row[5],
                'valoracion': row[6],
                'favorito': row[7],
                'reseña': row[8],
                'compartido': row[9]
            }
        
        return pelicula

    def modificar_pelicula(self, id, columna, valor):
        update = f"UPDATE pelicula SET { columna } = %s WHERE id = %s"
        self.cursor.execute(update, (valor, id))
        self.connection.commit()

        return self.cursor.rowcount

    def eliminar_pelicula(self, id):
        delete = "DELETE FROM pelicula WHERE id = %s"
        self.cursor.execute(delete, (id,))
        self.connection.commit()

        return self.cursor.rowcount

    def get_peliculas_usuario(self, id):
        query = "SELECT * FROM pelicula WHERE usuarioId = %s"
        self.cursor.execute(query, (id,))

        peliculas = []
        for row in self.cursor.fetchall():
            pelicula = {
                'id': row[0],
                'titulo': row[1],
                'fecha_visto': row[2],
                'imagen': row[3],
                'director': row[4],
                'año': row[5],
                'valoracion': row[6],
                'favorito': row[7],
                'reseña': row[8],
                'compartido': row[9]
            }
            peliculas.append(pelicula)

        return peliculas


    def __del__(self):
        self.connection.close()