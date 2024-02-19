from random import randint

m1 = {}
m2 = {}

qtde_linhas = int(input("Quantas linhas para a primeira matriz: "))
qtde_colunas = int(input("Quantas colunas para a primeira matriz: "))

qtde_linhas2 = int(input("Quantas linhas para a segunda matriz: "))
qtde_colunas2 = int(input("Quantas colunas para a segunda matriz: "))

for i in range(qtde_linhas):
    for j in range(qtde_colunas):
        m1[(i,j)] = randint(1,20)

for i in range(qtde_linhas2):
    for j in range(qtde_colunas2):
        m2[(i,j)] = randint(1,20)

print('Matriz 1->')
for a in range(0,qtde_linhas):
    for b in range(0,qtde_colunas):
      
        print(m1[(a,b)], end = ' ')
    print()
print("="*30)
print('Matriz 2->')
for a in range(0,qtde_linhas2):
    for b in range(0,qtde_colunas2):
      
        print(m2[(a,b)], end = ' ')
    print()

if qtde_colunas != qtde_colunas2:
    print("Matrizes com dimensões diferentes!")
else:
    resultado = {}
    for i in range(qtde_linhas):
        for j in range(qtde_colunas2):
            multi = 0
            for k in range(qtde_colunas):
                multi += m1[(i,k)] * m2[(k,j)]
            resultado[(i,j)] = multi
print("="*30)
print("Multiplicação->")
for i in range(qtde_linhas):
    for j in range(qtde_colunas2):
        print(resultado[(i,j)], end = ' ')
    print()