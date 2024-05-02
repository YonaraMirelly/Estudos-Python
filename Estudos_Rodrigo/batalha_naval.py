
def identificar(tabuleiro, i, j, linha, coluna, identificador):
    celulas = 0
    # caso base para a borda
    if i < linha and i >= 0 and j < coluna and j >=0:
        #caso base para o navio já identificado ou água
        if tabuleiro[i][j] == '#':
            tabuleiro[i][j] == identificador
            celulas +=1
            # indo para a direita
            celulas += identificar(tabuleiro, i, j+1,  identificador, linha, coluna)
            # indo para baixo
            celulas += identificar(tabuleiro, i+1, j, identificador, linha, coluna)
            # indo para esquerda
            celulas += identificar(tabuleiro, i, j-1, identificador, linha, coluna)
            # indo para cima
            celulas += identificar(tabuleiro, i-1, j,  identificador, linha, coluna)

    return celulas
def principal():
    linha, coluna = [int(i) for i in input().split()]
    tabuleiro = [[j for j in input()] for _ in range(linha)]
    tiros = int(input())
    tamanhos_dic = {}
    identificare = 0
    for _ in range(tiros):
        # -1 pois a matriz começa com 0 na minha conta kk
        i, j  = [int(x)-1 for x in input().split()]
        if tabuleiro[i][j] == '#':
            tamanho_navio = identificar(tabuleiro, i, j, identificador, linha, coluna)
            tamanhos_dic[identificador] = tamanho_navio - 1 
            identificare += 1
        elif tabuleiro[i][j] != '.':
            tamanhos_dic[tabuleiro[i][j]] -= 1
    destruidos = 0
    for tamanho in tamanhos_dic.values():
        if tamanho == 0:
            destruidos += 1
    print(destruidos)

if __name__ == '__main__':
    principal()