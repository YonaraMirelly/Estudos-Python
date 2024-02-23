n = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
lista = (n, n2, n3, n4)
print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes.')

if 3 in lista:
    print(f'O valor 3 foi apareceu na {lista.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi encontrado.')
print(f'Os valores PARES digitados foram ' , end = '')
for numeros in lista:
    if numeros % 2 ==0:
        print(f'[{numeros}]', end = ' ')
input()