
n = int(input())
incompleta = [int(i) for i in input().split()]
soma_completa = int(n * (n + 1) /2 )
soma_incompleta = 0
for i in incompleta:
    soma_incompleta += i
falta = soma_completa - soma_incompleta
print(falta)