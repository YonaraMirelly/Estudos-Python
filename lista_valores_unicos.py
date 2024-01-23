lista = []
opçao = 'S'
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opçao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opçao in'Nn':
       break
print('='*30)
lista.sort()
print(f'Os valores adicionados foram {lista} :)')
input()

