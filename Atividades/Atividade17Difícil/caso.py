#17) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o número de filhos. Faça uma função que leia esses dados para um número não determinado de pessoas e retorne a média de salário da população, a média do número de filhos, o maior salário e o percentual de pessoas com salário inferior à R$380,00.

def calcular_estatisticas():
    total_salarios = 0
    total_filhos = 0
    quantidade_pessoas = 0
    salario_maior = float('-inf')
    quantidade_salario_inferior_380 = 0

    while True:
        salario = float(input("Digite o salario da pessoa (ou -1 para encerrar): "))
        if salario == "calcular":
            break
        quantidade_pessoas += 1
        total_salarios += salario
        if salario > salario_maior:
            salario_maior = salario
        if salario < 380:
            quantidade_salario_inferior_380 += 1

        num_filhos = int(input("Digite o número de filhos da pessoa: "))
        total_filhos += num_filhos

    media_salario = total_salarios / quantidade_pessoas if quantidade_pessoas > 0 else 0
    media_filhos = total_filhos / quantidade_pessoas if quantidade_pessoas > 0 else 0
    percentual_salario_inferior_380 = (quantidade_salario_inferior_380 / quantidade_pessoas) * 100 if quantidade_pessoas > 0 else 0

    return media_salario, media_filhos, salario_maior, percentual_salario_inferior_380

media_salario, media_filhos, salario_maior, percentual_salario_inferior_380 = calcular_estatisticas()

print("Média de salário da população:", media_salario)
print("Média do número de filhos:", media_filhos)
print("Maior salário:", salario_maior)
print("Percentual de pessoas com salário inferior a R$380,00:", percentual_salario_inferior_380, "%")
