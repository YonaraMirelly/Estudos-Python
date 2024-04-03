n = int(input())
lista = [int(i) for i in input().split()]
a, b = 0, 0
for numero in lista:
    if numero == 1:
        a = 1 - a
    elif numero == 2:
        a = 1 - a
        b = 1 - b

print(a)
print(b)