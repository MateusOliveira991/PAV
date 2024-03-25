"12) Crie uma função que receba como parâmetro dois valores X e A" 
#calcule e retorneXa sem utilizar funções ou operadores de potência prontos."
def calculo_potencia(X:int, A:int) -> int:
    "Calculo da potencia"
    resultado = 1
    for i in range(A):
        resultado *= X
    return resultado
numero_base = int(input("Numero base:"))
numero_potencia = int(input("Numero potencia:"))
print(f"Calculo:{calculo_potencia(numero_base,numero_potencia )}")
