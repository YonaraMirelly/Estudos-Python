


a, b = [int(i) for i in input().split()]
n = int(input('Número a ser analisado -> '))
digitos = [int(d) for d in str(n)]

maior = 0
lista_maiores =[]

while len(lista_maiores) != (a-b):
    for c in digitos:
        if c>maior:
            maior=c
    digitos = [x for x in digitos if x != maior]
    lista_maiores += [maior]
    maior = 0

for j in lista_maiores:
    print(j, end='')

