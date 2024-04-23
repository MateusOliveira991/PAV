#Crie uma função que receba como parâmetro a altura (alt) e o sexo de uma pessoa e retorne o seu peso ideal. Para homens, deverá calcular o peso ideal usando a fórmula:peso ideal = 72.7 * alt - 58; para mulheres: peso ideal = 62.1 * alt - 44.7.

def pesoIdeal(altura, sexo):
    if sexo == 'masculino':
        peso_ideal = 72.7 * altura - 58
    elif sexo == 'feminino':
        peso_ideal = 62.1 * altura - 44.7
    else:
        return "Sexo não reconhecido. Por favor, informe 'homem' ou 'mulher'."

    return peso_ideal


altura = float(input("Informe a altura (com ponto separando metros de centimetros) "))
sexo = input("Informe o sexo ('masculino' ou 'feminino'): ")


peso_ideal = pesoIdeal(altura, sexo)


print(f"O peso ideal para uma pessoa do sexo {sexo} com altura de {altura}m é: {peso_ideal} kg")
