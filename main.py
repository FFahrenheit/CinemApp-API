from flask import Flask, json, jsonify, request
from db.connection import Database

def run_server():
    app = Flask(__name__)
    bd = Database()

    @app.route('/api/v1/usuarios', methods=['POST'])
    def usuario():
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


    app.run(debug=True)

if __name__ == '__main__':
    run_server()