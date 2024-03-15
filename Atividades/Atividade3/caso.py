#Crie uma função que receba um valor e informe se ele é positivo ou não.

def verificar_positivo(valor):
    if valor > 0:
        return "O valor é positivo."
    elif valor == 0:       #Elif???
        return "O valor é zero."
    else:
        return "O valor é negativo."


valor = float(input("Digite um valor: "))
resultado = verificar_positivo(valor)
print(resultado)