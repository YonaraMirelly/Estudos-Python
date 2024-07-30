def busca(fazenda, visitado, x, y, R, C):
    # Movimentos possíveis (cima, baixo, esquerda, direita)
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    pilha = [(x, y)] # começa com a célula inicial
    # número de ovelhas e lobos na região
    ovelhas = 0 
    lobos = 0
    # atualizar a quantidade de ovelhas e lobos
    if fazenda[x][y] == 'k':
        ovelhas += 1
    elif fazenda[x][y] == 'v':
        lobos += 1
    
    while pilha: # enquanto houver células na pilha
        cx, cy = pilha.pop() # remover célula
        for dx, dy in movimentos:
            nx, ny = cx + dx, cy + dy # verificar células vizinhas
            if 0 <= nx < R and 0 <= ny < C and not visitado[nx][ny] and fazenda[nx][ny] != '#':
                visitado[nx][ny] = True
                pilha+= [(nx, ny)]
                if fazenda[nx][ny] == 'k': # atualizar quando necessário
                    ovelhas += 1
                elif fazenda[nx][ny] == 'v':
                    lobos += 1
    
    return ovelhas, lobos # número de ovelhas e lobos encontrados na região

def resolver_fazenda(fazenda, R, C): # número de ovelhas e lobos sobreviventes
    visitado = [[False] * C for _ in range(R)] # matriz pra acompanhar as células já visitadas
    # lobos e ovelhas já sobreviventes
    ovelhas_total = 0
    lobos_total = 0
    
    for i in range(R):
        for j in range(C):
            if not visitado[i][j] and fazenda[i][j] != '#': # para cada célula não visitada, realizar uma busca
                visitado[i][j] = True
                ovelhas, lobos = busca(fazenda, visitado, i, j, R, C)
                if ovelhas > lobos: # atualizar os contadores
                    ovelhas_total += ovelhas
                else:
                    lobos_total += lobos
    
    return ovelhas_total, lobos_total

# leitura da entrada
R, C = map(int, input().split())
fazenda = [input().strip() for _ in range(R)]

# resolvendo o problema
ovelhas, lobos = resolver_fazenda(fazenda, R, C)

# imprimindo o resultado
print(ovelhas, lobos)
