
def soma(lista):
    s = 0
    for i in lista:
        s += i
    return s

quantidade_colunas = int(input()) 
colunas = [int(i) for i in input().split()] 
quantidade_blocos = soma(colunas) 
escada_blocos = int((quantidade_colunas + 1) * quantidade_colunas / 2) 

if ((quantidade_blocos - escada_blocos) % quantidade_colunas) != 0:
    print(-1)
else:
    base_escada = int((quantidade_blocos - escada_blocos) / quantidade_colunas)
    n_movimentos = 0
    for idx, coluna in enumerate(colunas):
        if coluna > (base_escada + idx + 1):
            n_movimentos += coluna - (base_escada + idx + 1)
    print(n_movimentos)