#Faça uma função que receba um número inteiro e positivo N como parâmetro e retorne a soma dos números inteiros existentes entre o número 1 e N (Inclusive).
def somaAte_N(N):
    soma=0

    for i in range(1,N+1):
        soma+=i
    return soma

N=5

resultado = somaAte_N(N)
print(resultado)
