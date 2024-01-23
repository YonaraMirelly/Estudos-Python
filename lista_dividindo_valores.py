lista = []
listapar = []
listaimpar = []
escolha = 'Ss'
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    if escolha in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)
print('='*40)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {listapar}.')
print(f'A lista de ímpares é {listaimpar}.')
input()