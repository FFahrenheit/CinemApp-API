from flask import Flask, json, jsonify, request
from db.connection import Database

def run_server():
    app = Flask(__name__)
    bd = Database()

    @app.route('/api/v1/usuarios', methods=['POST'])
    @app.route('/api/v1/usuarios/<int:id>/peliculas', methods = ['GET'])
    def usuario(id = None):
        if request.method == 'POST' and request.is_json:
            try:
                data = request.get_json()
                print(data)

                if bd.crear_usuario(data['correo'], data['contraseña']):
                    return jsonify({'code': 'ok'})
                else:
                    return jsonify({'code': 'existe'})
            except:
                return jsonify({'code': 'error'})
        elif request.method == 'GET' and id is not None:
            return jsonify(bd.get_peliculas_usuario(id))

    @app.route('/api/v1/peliculas', methods=['GET', 'POST'])
    @app.route('/api/v1/peliculas/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
    def peliculas(id = None):
        if request.method == 'POST' and request.is_json:
            try:
                data = request.get_json()
                print(data)

                if bd.insertar_pelicula(data):
                    return jsonify({ 'code': 'ok' })
                else:
                    return jsonify({'code': 'no'})
            except Exception as e:
                print(e)
                return jsonify({'code': 'error'})

        elif request.method == 'GET' and id is None:
            return jsonify(bd.get_peliculas())
        elif request.method == 'GET' and id is not None:
            return jsonify(bd.get_pelicula(id))
        elif request.method == 'PATCH' and id is not None and request.is_json:
            data = request.get_json()
            column = data['columna']
            value = data['valor']

            if bd.modificar_pelicula(id, column, value):
                return jsonify(code='ok')
            else:
                 return jsonify(code='error')
        elif request.method == 'DELETE' and id is not None:
            if bd.eliminar_pelicula(id):
                return jsonify(code='ok')
            else:
                return jsonify(code='error')
 
    @app.route('/api/v1/sesiones', methods=['POST'])
    def sesion():
        if request.method == 'POST' and request.is_json:
            try:
                data = request.get_json()
                correo = data['correo']
                contra = data['contraseña']

                id, ok = bd.iniciar_sesion(correo, contra)

                if ok:
                    return jsonify({'code': 'ok', 'id': id})
                else:
                    return jsonify({'code': 'noexiste'})
            except:
                return jsonify({'code': 'error'})

    app.run(debug=True)

if __name__ == '__main__':
    run_server()