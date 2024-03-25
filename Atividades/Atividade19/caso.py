#19) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em um vetor. O programa deverá calcular e mostrar a maior e a menor temperatura do ano, juntamente com o mês em que elas ocorreram (o mês deverá ser mostrado por extenso: 1 = janeiro; 2 = fevereiro; ...).
#OBSERVAÇÃO: Não se preocupe com empates

def mes_extenso (mes): 
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return meses[mes-1] 

def temperatura_maior_menor():
    temperaturas = []

    for i in range(1, 13):
        temperatura = float(input(f"Digite a temperatura média do mês {mes_extenso(i)}: "))
        temperaturas.append((temperatura, i))

    maior_temperatura = max(temperaturas)
    menor_temperatura = min(temperaturas)

    print(f"A maior temperatura do ano foi {maior_temperatura[0]} graus, no mês de {mes_extenso(maior_temperatura[1])}")
    print(f"A menor temperatura do ano foi {menor_temperatura[0]} graus, no mês de {mes_extenso(menor_temperatura[1])}")

temperatura_maior_menor()