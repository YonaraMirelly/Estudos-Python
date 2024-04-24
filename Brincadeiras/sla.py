n = int(input())
lista = []
for i in range(n):
    lista += [[int(i) for i in input().split()]]

soma_linhas = 0
for x in lista[0]:
    soma_linhas += x
soma_reserva = 0
# analisa todas as linhas
for i in range(1, n):
    for x in lista[i]:
        soma_reserva += x
        if soma_reserva != soma_linhas:
            print(-1)
# analisa todas as colunas
soma_coluna = 0
for j in range(n):
    for i in range(n):
        for x in lista[i][j]:
            soma_coluna += x
            if soma_coluna != soma_linhas:
                print(-1)

# primeira diagonal
soma_diagonal = 0
for i in range(n):
    for i in range(n):
        for x in lista[i][i]:
            soma_diagonal += x
            if soma_diagonal != soma_linhas:
                print(-1)

# segunda diagonal
soma_diagonal2 = 0
for i in range(n):
    for i in range(n):
        for x in lista[i][n-i-1]