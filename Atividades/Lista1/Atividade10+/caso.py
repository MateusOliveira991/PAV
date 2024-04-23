
#Elabore uma função que leia um número não determinado de valores positivos e retorne a média aritmética desses valores.
def calcular_media_aritmetica():
    soma = 0
    quantidade = 0

    while True:
        valor = float(input("Digite um valor positivo (digite um número negativo ou zero para sair): "))
        
        if valor <= 0:
            break  # Como finalizar se não for usando o If e o break?
        soma += valor
        quantidade += 1

    if quantidade == 0:
        return "Nenhum valor positivo foi fornecido."

    media = soma / quantidade
    return media


media = calcular_media_aritmetica()


print("A média aritmética dos valores positivos fornecidos é:", media)

# Como finalizar se não for usando o If e o break?