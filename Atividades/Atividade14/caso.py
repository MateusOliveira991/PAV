#14) Elabore uma função que receba um vetor X de 15 números inteiros e retorne a
#quantidade de valores pares em X.

def contabiliza_pares(x: list) -> int:
    qtd_pares=0
    for numero in lista_numeros:
        if numero % 2==0:
            qtd_pares+=1
    return qtd_pares
        
lista_numeros=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
total_pares = contabiliza_pares(lista_numeros)
print(f"Total pares = {total_pares}")