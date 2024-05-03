from flask import Flask

app = Flask(__name__)

# Executar flask --app ExemploAPI.py run 
@app.route("/", methods=['POST'])
def hello_world():
    return "Hello, World!"

@app.route("/PAV", methods=['GET'])
def welcome():
    return "Welcome to PAV!"
