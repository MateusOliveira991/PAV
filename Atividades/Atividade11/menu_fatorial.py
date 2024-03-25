"11) Faça uma função que receba um valor inteiro e positivo, calcule e mostre o seu fatorial."
def calculo_fatorial(valor: int) -> str:
    "Calcula o fatorial do numero"
    resultado = 1
    for i in range(1, valor+1):
        resultado *= i
    return resultado

numero = int(input("Informe o numero: "))
print(calculo_fatorial(numero))
