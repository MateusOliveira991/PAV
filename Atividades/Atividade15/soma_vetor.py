"15) Faça uma função que receba um vetor X de 20 de números reais como parâmetro e retorne a soma dos elementos de X."
def calculo_vetor(vetor: list[20]):
    "Calcula o valores dentro do vetor"
    resultado = 0.0
    for i in range(0, len(vetor).numerator):
        resultado += vetor[i]
    return resultado
values = [0.1, 0.1, 0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
valor_final = calculo_vetor(values)
valor_formatado = "{:.2f}".format(valor_final)
print(f"Valor do vetor: {valor_formatado}")
