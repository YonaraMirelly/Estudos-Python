def max_planetas(M, N, planos, planetas):
    contagem_regioes = {}
    for planeta in planetas:
        x, y, z = planeta
        chave_regiao = []
        for plano in planos:
            A, B, C, D = plano
            valor = A * x + B * y + C * z - D
            if valor > 0:
                chave_regiao.append(1)  
            else:
                chave_regiao.append(0)  
        chave_regiao = tuple(chave_regiao)
        if chave_regiao in contagem_regioes:
            contagem_regioes[chave_regiao] += 1
        else:
            contagem_regioes[chave_regiao] = 1
    return max(contagem_regioes.values())
M, N = map(int, input().split())
planos = [tuple(map(int, input().split())) for _ in range(M)]
planetas = [tuple(map(int, input().split())) for _ in range(N)]
print(max_planetas(M, N, planos, planetas))
