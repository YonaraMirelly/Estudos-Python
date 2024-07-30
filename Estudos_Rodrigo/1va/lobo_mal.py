def dfs(fazenda, visitado, x, y, R, C):
    # movimentos possíveis (cima, baixo, esquerda, direita)
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    stack = [(x, y)]
    ovelhas = 0
    lobos = 0
    
    if fazenda[x][y] == 'k':
        ovelhas += 1
    elif fazenda[x][y] == 'v':
        lobos += 1
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in movimentos:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < R and 0 <= ny < C and not visitado[nx][ny] and fazenda[nx][ny] != '#':
                visitado[nx][ny] = True
                stack.append((nx, ny))
                if fazenda[nx][ny] == 'k':
                    ovelhas += 1
                elif fazenda[nx][ny] == 'v':
                    lobos += 1
    
    return ovelhas, lobos

def resolver_fazenda(fazenda, R, C):
    visitado = [[False] * C for _ in range(R)]
    ovelhas_total = 0
    lobos_total = 0
    
    for i in range(R):
        for j in range(C):
            if not visitado[i][j] and fazenda[i][j] != '#':
                visitado[i][j] = True
                ovelhas, lobos = dfs(fazenda, visitado, i, j, R, C)
                if ovelhas > lobos:
                    ovelhas_total += ovelhas
                else:
                    lobos_total += lobos
    
    return ovelhas_total, lobos_total

# Leitura da entrada
R, C = map(int, input().split())
fazenda = [input().strip() for _ in range(R)]

# Resolvendo o problema
ovelhas, lobos = resolver_fazenda(fazenda, R, C)

# Imprimindo o resultado
print(ovelhas, lobos)
