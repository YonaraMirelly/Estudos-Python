i = 0
a = 0

ganhador = int(input())
lista = list(map(int, input().split()))

while a < ganhador:
    a += lista[i]
    i += 1

print(i)