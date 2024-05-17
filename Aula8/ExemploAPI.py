from flask import Flask
from flask import request

app = Flask(__name__)


funcionario = [{"id":"1", "nome":"Douglas"}, {"id":"2", "nome":"Kauan"}]

# Executar flask --app ExemploAPI.py run 
@app.route("/funcionario/<id>/<nome>", methods=['POST'])
def createUrl(id: int, nome: str):
    novoFuncionario = {"id": id, "nome": nome}
    funcionario.append(novoFuncionario)
    return funcionario

# Rota para cadastro de funcionario
@app.route("/funcionario", methods=['POST'])
def create():
    funcionario.append(request.form)
    return funcionario

## Rota que recebe como parâmetro o nome e retorna os dados do funcionário que possui esse nome.
@app.route("/funcionario/nome/<nome>", methods=['GET'])
def getByName(nome: str):
    for i in range(0, len(funcionario)):
        if funcionario[i]["nome"] == nome:
            return funcionario[i]
    return {}

## Rota que recebe como parâmetro o id e retorna os dados do funcionário que possui esse id.
@app.route("/funcionario/<id>", methods=['GET'])
def getById(id: int):
    for i in range(0, len(funcionario)):
        if funcionario[i]["id"] == id:
            return funcionario[i]
    return {}

@app.route("/funcionario", methods=['GET'])
def getAll():
    return funcionario

# Rota para atualização de um funcionario
@app.route("/funcionario/<id>", methods=['PUT'])
def update(id: int):
    for i in range(0, len(funcionario)):
        if funcionario[i]["id"] == id:
            funcionario[i]["nome"] = request.form["nome"]

    return funcionario

# Rota para excluir um funcionario
@app.route("/funcionario/<id>", methods=['DELETE'])
def delete(id: int):
    for i in range(0, len(funcionario)):
        if funcionario[i]["id"] == id:
            del funcionario[i]
            return funcionario


#Exercício: UM endpoint busca de funcionários por parâmetros. 
# (id ou nome) Ex: localhost:5000/funcionario?nome=Douglas


@app.route("/funcionario", methods=['GET'])
def getFuncionario():
    if "id" in request.args:
        return getById(request.args["id"])
    elif "nome" in request.args:
        return getByName(request.args["nome"])
    return {}
