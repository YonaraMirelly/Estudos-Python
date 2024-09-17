def descobrir(matriz_fazenda, i, j, linhas, colunas, total_ovelhas, total_lobos, grupo_atual):
    if i <= 0 or j <= 0:
        return
    elif i >= linhas or j >= colunas:
        return
    elif matriz_fazenda[i][j] == 'v' or matriz_fazenda[i][j] == '.' or matriz_fazenda[i][j] == 'k':
        if matriz_fazenda[i][j] == 'v':
            total_ovelhas[grupo_atual] += 1
            matriz_fazenda[i][j] = grupo_atual
        elif matriz_fazenda[i][j] == 'k':
            total_lobos[grupo_atual] += 1
            matriz_fazenda[i][j] = grupo_atual
        elif matriz_fazenda[i][j] == '.':
            matriz_fazenda[i][j] = grupo_atual
        descobrir(matriz_fazenda, i-1, j, linhas, colunas, total_ovelhas, total_lobos, grupo_atual)
        descobrir(matriz_fazenda, i+1, j, linhas, colunas, total_ovelhas, total_lobos, grupo_atual)
        descobrir(matriz_fazenda, i, j-1, linhas, colunas, total_ovelhas, total_lobos, grupo_atual)
        descobrir(matriz_fazenda, i, j+1, linhas, colunas, total_ovelhas, total_lobos, grupo_atual)

    else:
        return
n = list(map(int, input().split()))
index1 = n[0]-1
index2 = n[1]-1
fazenda = list(range(n[0]))
for i in range(n[0]):
    fazenda[i] = list(input())

grupo_atual=0
lobo = 0
ovelha = 0
total_ovelhas = []
total_lobos = []
for i in range(n[0]):
    for c in range(n[1]):
        if fazenda[i][c] == '.' or fazenda[i][c] == 'v' or fazenda[i][c] == 'k':
            total_ovelhas.append(0)
            total_lobos.append(0)
            descobrir(fazenda, i, c, index1, index2, total_ovelhas, total_lobos, grupo_atual)
            if total_ovelhas[grupo_atual] >= total_lobos[grupo_atual]:
                lobo += total_ovelhas[grupo_atual]
                ovelha += 0
            elif total_lobos[grupo_atual] > total_ovelhas[grupo_atual]:
                lobo += 0
                ovelha += total_lobos[grupo_atual]
            grupo_atual += 1
print(ovelha, lobo)