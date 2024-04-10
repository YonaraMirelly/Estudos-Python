contador = 0

def F(n):
    if n == 1:
        return G(0)
    elif n % 2 == 0:
        G(1)
        return F(n/2)
    elif n % 2 != 0:
        G(1)
        return F(3 * n + 1)
    
def G(c):
    global contador
    contador +=c
    return contador

T = int(input())
maior = 0
lista = []
for i in range(T):
    periodo = [int(x) for x in input().split()]
    for j in range(periodo[0], periodo[1]):
        contador = 0
        a = F(j)
        if a>maior:
            maior = a
            a = 0
    lista += [maior+1]
    maior = 0

for x in range(T):
    print(f'Caso {x+1}: {lista[x]}')
