m = {}

qtde_linha = int(input("Quantas linhas: "))
qtde_coluna = int(input("Quantas colunas: "))

for i in range(qtde_linha):
    for j in range(qtde_coluna):
        elemento = int(input(f"[{i},{j}] = "))
        m[(i,j)] = elemento

print('MATRIZ->')
for i in range(qtde_linha):
    for j in range(qtde_coluna):
        print(m[(i,j)], end = ' ')
    print()

#lista com a média aritmética de cada uma das linhas
lista = []

for i in range(qtde_linha):
    media = 0
    for j in range(qtde_coluna):
        media += m[(i,j)]
    media /=qtde_coluna
    lista.append(media)

print(lista)