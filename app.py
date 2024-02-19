from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

usuarios = []

def novo_usuario(cpf: int, nome: str, data_nascimento: datetime):
    return { "cpf":cpf, "nome":nome, "data_nascimento":data_nascimento.isoformat() }

@app.route('/')
def index():
    return "<h1>API - BD</h1>"

@app.route('/users', methods=['POST'])
def create_users():
    if request.method == 'POST':
        cpf = int(request.form['cpf'])
        nome = request.form['nome']
        data_nascimento = datetime.strptime(request.form['data_nascimento'], '%Y-%m-%d')
        
        usuarios.append(novo_usuario(cpf, nome, data_nascimento))
        return jsonify({'sucess': f"user: {cpf} created."}),  201

@app.route('/users/<int:cpf>', methods=['GET'])
def get_user(cpf):
    if request.method == 'GET':
        for usuario in usuarios:
            if usuario['cpf'] == cpf:
                return jsonify(usuario)
        return "Not Found",  404

if __name__ == '__main__':
    app.run()
