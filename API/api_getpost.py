from flask import Flask

app = Flask(__name__)

@app.route("/oi", methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route("/funcionario/<int:id>", methods=['GET'])
def getById(id:int):
    funcionario = [
        {
            "id": "1",
            "nome": "Mateus",
        },
        {
            "id": "2",
            "nome": "Joao",
        },
        
    ]
    
    for i in range(0, len(funcionario)):
        if int (funcionario[i]["id"] )== id:
            return funcionario[i]
    return {"message": "Funcionario nao encontrado!"}

#Rota para atualização de funcionario
# testando o metodo post e o metodo put um de cada vez
@app.route("/funcionario/<int:id>", methods=['POST'])

def updateById(id:int):
    funcionario = [
        {
            "id": "1",
            "nome": "Mateus",
        },
        {
            "id": "2",
            "nome": "Joao",
        },
        
    ]
    for i in range(0, len(funcionario)):
        if int (funcionario[i]["id"] )== id:
            funcionario[i]["nome"] = "Atualizado"
            return funcionario[i]
    return {"message": "Funcionario nao encontrado!"}


