# ok
def identificar(tabuleiro, i, j, linha, coluna, identificador):
    celulas = 0
    #  borda
    if linha > i >= 0 and coluna > j >=0:
        # navio já identificado ou água
        if tabuleiro[i][j] == '#':
            tabuleiro[i][j] = identificador
            celulas +=1
            # indo para a direita
            celulas += identificar(tabuleiro, i, j+1, linha, coluna, identificador)
            # indo para baixo
            celulas += identificar(tabuleiro, i+1, j, linha, coluna, identificador)
            # indo para esquerda
            celulas += identificar(tabuleiro, i, j-1, linha, coluna, identificador)
            # indo para cima
            celulas += identificar(tabuleiro, i-1, j, linha, coluna, identificador)
    return celulas
def main():
    linha, coluna = [int(i) for i in input().split()]
    tabuleiro = [[j for j in input()] for _ in range(linha)]
    tiros = int(input())
    dic = {}
    identificador = 0
    for _ in range(tiros):
        # -1 pois a matriz começa com 0 na minha conta
        i, j  = [int(x)-1 for x in input().split()]
        tamanho_navio = identificar(tabuleiro, i, j, linha, coluna, identificador)
        if tamanho_navio > 0:
            dic[identificador] = tamanho_navio - 1 
            identificador += 1
        elif tabuleiro[i][j] != '.':
            dic[tabuleiro[i][j]] -= 1
    # contagem dos navios destruídos
    destruidos = 0
    for tamanho in dic.values():
        if tamanho == 0:
            destruidos += 1
    print(destruidos)
if __name__ == "__main__":
    main()