
n = int(input())

matriz = [[int(value) for value in input().split()] for i in range(n)]
linha = [sum(matriz[i]) for i in range(n)]
valorCorreto = sorted (linha)[1]

for i in  range(n):
    if sum(matriz[i]) != valorCorreto:
        errado = i 
        soma_errada = sum(matriz[i]) 

for j in range(n):
    if sum([matriz[i][j] for i in range(n)]) != valorCorreto:
        errado2 = j

print (valorCorreto - (soma_errada - matriz[errado][errado2]), matriz[errado][errado2])
