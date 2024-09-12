def Maior_diferenca(N, diferencas):
    diferencamaxima = 0
    diferenca_atual = 0

    for i in range(2 * N):
        diferenca_atual += diferencas[i % N]
        if diferenca_atual < 0:
            diferenca_atual = 0
        if diferenca_atual > diferencamaxima:
            diferencamaxima = diferenca_atual

    return diferencamaxima
N = int(input())
diferencas = list(map(int, input().split()))
resultado = Maior_diferenca(N, diferencas)
print(resultado)