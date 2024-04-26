#Crie uma função que receba dois valores e informa se o primeiro valor é divisível pelo segundo ou não.

def divisivel( valor1, valor2):
    if valor2 == 0:
        return "Denominator cannot be zero."

    
    if valor1 % valor2== 0:
        return f"O {valor1} é divisível por {valor2}."
    else: return f"O {valor1} NÃO é divisível por {valor2}."

    #f dentro de return é para formatar a string, para que os valores das variáveis sejam impressos na string. ({valor1}).

valor1 = float(input("Digite um número:"))
valor2= float(input("Digite outro número:"))
resultado = divisivel(valor1 , valor2)
print(resultado)

#como tirar o zero depois da virgula?



