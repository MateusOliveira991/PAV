#8) 16) Crie uma função que gere e mostre os dez primeiros números primos acima de 100.

def primo(numero):
    if numero <= 1:
        return False
    elif numero<=3:
        return True
    elif numero%2 == 0 or numero%3 == 0:
        return False
    i = 5
    while i*i <= numero:
        if numero%i == 0 or numero%(i+2) == 0:
            return False
        i += 6
    return True

def primos():
    contador = 0
    numero = 101
    while contador < 10:
        if primo(numero):
            print(numero)
            contador += 1
        numero += 1

primos()