


# a, b = [int(i) for i in input().split()]
# n = int(input('Número a ser analisado -> '))
# digitos = [int(d) for d in str(n)]

# maior = 0
# lista_maiores =[]

# while len(lista_maiores) != (a-b):
#     for c in digitos:
#         if c>maior:
#             maior=c
#     digitos = [x for x in digitos if x != maior]
#     lista_maiores += [maior]
#     maior = 0

# for j in lista_maiores:
#     print(j, end='')

def maior(a, b, lista):
    qtde_dig = a-b
    maior = 0
    maiores = []
    while len(maiores) != qtde_dig:
        for c in lista:
            if c>maior:
                maior=c
        lista = [x for x in lista if x != maior]
        maiores += [maior]
        maior = 0
    return maiores

casos = []

a, b = [int(i) for i in input().split()]
n = int(input('Número a ser analisado -> '))
digitos = [int(d) for d in str(n)] 
casos += [maior(a, b, digitos)]

for caso in casos:
    for digito in caso:
        print(digito, end='')
    print()
    

