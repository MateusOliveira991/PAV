#13) Foi realizada uma pesquisa entre quinze habitantes de uma região. Foram
#coletados estes dados de cada habitante: idade, sexo, salário e número de filhos. Faça
#uma função que leia esses dados armazenando-os em vetores. Depois, crie funções
#que recebam esses parâmetros e retornem a média de salário entre os habitantes, a
#menor e a maior idade do grupo e a quantidade de mulheres com três filhos que
#ecebem até R$ 500,00 (utilize uma função para cada cálculo).
"Atividade 13"
class registro_pessoa():
    "Objeto registro Pessoa"
    def __init__(self, idade:int,sexo: str, salario:float, n_filhos:int) -> None:
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
        self.n_filhos = n_filhos
    def salario_medio(self, pessoas:list) -> float:
        "Calcula o salario medio"
        for pessoa in pessoas:
           salario_media = [pessoa.salario]
        media = sum(salario_media) /len(pessoas)
        return media
    def menor_idade(self, pessoas:list) -> int:
        "Verifica menor de idade"
        for pessoa in pessoas:
            menor_idade = [pessoa.idade]
        idade = min(menor_idade)
        return idade
    def maior_idade(self, pessoas:list):
        "Verifica maior de idade"
        for pessoa in pessoas:
            menor_idade = [pessoa.idade]
        idade = max(menor_idade)
        return idade
    def mulheres_tres_filhos_ate_500(self,pessoas: list) -> list:
        "Verifica quantidade de mulheres com 3 filhos com 500 reais"
        mulheres = [pessoa for pessoa in pessoas if pessoa.sexo == 'F' and pessoa.n_filhos == 3 and pessoa.salario <= 500.0]
        return mulheres

def selecao_registro():
    "Escolha"
    registros = []
    escolha_de_alternativa = int(input("1 - Cadastro manual\n"+
                                       "2 - Cadastro automatico\n"+
                                       "Escolha a operação desejada:"))
    if escolha_de_alternativa == 1:
        for i in range(15):
            idade = int(input("Digite a idade:"))
            while True:
                sexo = str(input("Digite F para feminino M para masculino:").upper())
                if sexo in ['F', 'M']:
                    break
                else:
                    print("Sexo invalido, insira novamente")
            salario = float(input("Digite o salario:"))
            n_filhos = int(input("Digite o numero de filhos:"))
            registros.append(registro_pessoa(idade,sexo,salario,n_filhos))
    if escolha_de_alternativa == 2:
        registros = [ registro_pessoa(idade=25, sexo='M', salario=3000.0, n_filhos=1),
        registro_pessoa(idade=30, sexo='F', salario=2500.0, n_filhos=2),
        registro_pessoa(idade=40, sexo='M', salario=4000.0, n_filhos=3),
        registro_pessoa(idade=35, sexo='F', salario=3500.0, n_filhos=2),
        registro_pessoa(idade=28, sexo='M', salario=2800.0, n_filhos=1),
        registro_pessoa(idade=32, sexo='F', salario=500.0, n_filhos=3),
        registro_pessoa(idade=45, sexo='M', salario=5000.0, n_filhos=3),
        registro_pessoa(idade=29, sexo='F', salario=2700.0, n_filhos=1),
        registro_pessoa(idade=33, sexo='M', salario=3300.0, n_filhos=2),
        registro_pessoa(idade=38, sexo='F', salario=3800.0, n_filhos=3),
        registro_pessoa(idade=42, sexo='M', salario=4200.0, n_filhos=2),
        registro_pessoa(idade=31, sexo='F', salario=3100.0, n_filhos=1),
        registro_pessoa(idade=37, sexo='M', salario=3700.0, n_filhos=2),
        registro_pessoa(idade=34, sexo='F', salario=3400.0, n_filhos=3),
        registro_pessoa(idade=26, sexo='M', salario=2600.0, n_filhos=1),
        ]
    pessoa = registro_pessoa(0,'',0,0)
    formatado = f"{pessoa.salario_medio(registros):.{3}f}"
    print(f"Salario médio:{formatado}")
    print(f"Menor idade:{pessoa.menor_idade(registros)}")
    print(f"Maior idade:{pessoa.maior_idade(registros)}")
    print(f"Numero de mulheres:{len(pessoa.mulheres_tres_filhos_ate_500(registros))}")

selecao_registro()
