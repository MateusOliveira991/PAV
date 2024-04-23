#8) Faça uma função que receba como parâmetro o raio de uma esfera, calcule e mostre no programa principal o seu volume: v = 4/3 * R3.

def calcular_volume_esfera(raio):
    volume = (4/3) * 3.14159 * (raio ** 3)
    return volume

raio = float(input("Digite o raio da esfera:"))
volume = calcular_volume_esfera(raio)

print(f"O volume da esfera com raio {raio} é: {volume:.2f}")




