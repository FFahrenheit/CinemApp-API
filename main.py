from flask import Flask, jsonify
from db.connection import Database

def run_server():
    app = Flask(__name__)
    bd = Database()

    @app.route('/')
    def hola():
        return '<b>Hola mundo!<b>'

    @app.route('/usuarios/<string:nombre>')
    def usuarios(nombre):
        return 'Hola %s' % nombre    

    @app.route('/api/v1/usuarios')
    def get_usuarios():
        usuarios  = bd.get_users()

        return jsonify(usuarios)

    app.run()

if __name__ == '__main__':
    run_server()