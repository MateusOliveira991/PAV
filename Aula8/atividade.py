from flask import Flask
from flask import request

app = Flask(__name__)


funcionario = [{"id":"1", "nome":"Mateus"}, {"id":"2", "nome":"Pedro"}, {"id":"3", "nome":"Douglas"}, 
               {"id":"4", "nome":"Kauan"}, {"id":"5", "nome":"Lucas"}, {"id":"6", "nome":"João"}, 
               {"id":"7", "nome":"Maria"}, {"id":"8", "nome":"Jose"}, {"id":"9", "nome":"Ana"}, 
               {"id":"10", "nome":"Paulo"}]


#Exercício: UM endpoint busca de funcionários por parâmetros. 
# (id ou nome) Ex: localhost:5000/funcionario?nome=Douglas
#pra rodar:  flask --app atividade.py run
#teste: http://127.0.0.1:5000/funcionario?nome=Mateus
#teste: http://127.0.0.1:5000/funcionario?id=9

@app.route("/funcionario", methods=['GET'])
def getFuncionario():
    id = request.args.get('id')
    nome = request.args.get('nome')
    if id:
        for i in range(0, len(funcionario)):
            if funcionario[i]["id"] == id:
                return funcionario[i]
    elif nome:
        for i in range(0, len(funcionario)):
            if funcionario[i]["nome"] == nome:
                return funcionario[i]
    return {}





