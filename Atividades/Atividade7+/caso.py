#7)Crie uma função que receba três números inteiros como parâmetros,representando horas, minutos e segundos e os converta em segundos. Exemplo: 2h, 40min e 10seg correspondem a 9.610 segundos.

def converteS(horas, minutos, segundos):
    return (horas*3600) + (minutos*60)+ segundos

horas = 1
minutos = 30
segundos = 12

resultado = converteS(horas, minutos, segundos)
print(f"{resultado } segundos")

#Por que o f aqui vai dentro e na questão 4 vai fora?