def eh_bissexto(ano):
    """Verifica se um ano é bissexto."""
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    else:
        return False

def contar_bissextos_ate_2010():
    """Conta quantos anos bissextos ocorreram desde o ano 1 até o ano 2010."""
    count = 0
    for ano in range(1, 2011):
        if eh_bissexto(ano):
            count += 1
    return count

def menu():
    """Função de menu para permitir ao usuário escolher qual função utilizar."""
    print("Escolha uma opção:")
    print("1. Verificar se um ano é bissexto.")
    print("2. Contar quantos anos bissextos ocorreram desde o ano 1 até o ano 2010.")
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == '1':
        ano = int(input("Digite o ano que deseja verificar: "))
        if eh_bissexto(ano):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    elif opcao == '2':
        qtd_bissextos = contar_bissextos_ate_2010()
        print(f"De 1 até 2010, ocorreram {qtd_bissextos} anos bissextos.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")


menu()