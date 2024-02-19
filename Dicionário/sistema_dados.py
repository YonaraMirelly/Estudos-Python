principal = {}
backup = {}

def imprimir_e_apagar_dic():
    print("Dicionário principal-> ")
    for chave, valor in principal.items():
        print(f'{chave}: {valor}')
    principal.clear()

while True:
    
    chave = str(input("Digite a chave: "))
    valor = str(input("Digite o valor: "))

    principal[chave] = valor
    backup[chave] = valor

    if len(principal) == 5:
        imprimir_e_apagar_dic()

    rep = str(input("Deseja continuar? ")).upper()
    if rep == 'NÃO':
        imprimir_e_apagar_dic()
        break
