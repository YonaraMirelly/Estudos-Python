# Função para verificar se uma parte do navio já foi destruída
def parte_destruida(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == '.':
        return True
    return False

# Função para verificar se um disparo atinge uma parte do navio
def atingir_navio(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == '#':
        return True
    return False

# Função principal para determinar o número de navios destruídos
def contar_navios_destruidos(tabuleiro, disparos):
    navios_destruidos = 0
    for disparo in disparos:
        linha, coluna = disparo
        if atingir_navio(tabuleiro, linha-1, coluna-1) and not parte_destruida(tabuleiro, linha-1, coluna-1):
            navios_destruidos += 1
            tabuleiro[linha-1][coluna-1] = '.'  # Atualizar o tabuleiro para indicar a parte destruída do navio
    return navios_destruidos

# Leitura da entrada
N, M = map(int, input().split())
tabuleiro = [list(input()) for _ in range(N)]
K = int(input())
disparos = [tuple(map(int, input().split())) for _ in range(K)]

# Contar navios destruídos
navios_destruidos = contar_navios_destruidos(tabuleiro, disparos)

# Imprimir o resultado
print(navios_destruidos)
