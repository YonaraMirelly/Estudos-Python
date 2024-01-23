lista = []
escolha = 'Ss'
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    if escolha in 'N':
        break
print('=-'*40)
print(f'Você digitou {len(lista)} números.')
lista.sort(reverse = True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 NÃO faz parte da lista.')
input()