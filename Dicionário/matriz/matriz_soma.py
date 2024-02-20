
m1 = {}
m2 = {}
mres = {}

i, j = 3,3


m1[(0,0)] = 1
m1[(0,1)] = 2
m1[(0,2)] = 3
m1[(1,0)] = 4
m1[(1,1)] = 5
m1[(1,2)] = 6
m1[(2,0)] = 10
m1[(2,1)] = 8
m1[(2,2)] = 9

for a in range(0,i):
    for b in range(0,j):
        print(f'[{m1[(a,b)]:10.3f}]', end = ' ')
    print()

soma_impares = 0
soma_pares = 0

for valor in m1.values():
    if valor % 2 == 0 :
        soma_pares +=valor
    else:
        soma_impares += valor

print(f'Soma dos pares-> {soma_pares}')
print(f'Soma dos impares-> {soma_impares}')

