from random import randint

m1 = {}


qtde_linhas = int(input('Linhas primeira matriz-> '))
qtde_coluna = int(input('Colunas primeira matriz-> '))


for i in range(qtde_linhas):
    for j in range(qtde_coluna):
        m1[(i,j)] = randint(1,10)


print('Primeira matriz')
for i in range(qtde_linhas):
    for j in range(qtde_coluna):
        print(f'{m1[(i,j)]:^5}', end = ' ')
    print()

#t

for i in range(qtde_coluna-1):
    m1[(1,i)], m1[(2,i)] = m1[(2,i)], m1[(1,i)]
print("Linha modificada->")
for i in range(qtde_linhas):
    for j in range(qtde_coluna):
        print(f'{m1[(i,j)]:^5}', end = ' ')
    print()

#trocar a 1 coluna pela 4 coluna
for i in range(qtde_linhas-1):
    m1[(i,0)], m1[(i,3)] = m1[(i,3)], m1[(i,0)]


print("Coluna modificada->")
for i in range(qtde_linhas):
    for j in range(qtde_coluna):
        print(f'{m1[(i,j)]:^5}', end = ' ')
    print()
