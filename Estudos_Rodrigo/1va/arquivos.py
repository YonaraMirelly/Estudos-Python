# ok
def ordenar_selecao(lista):
    """ Ordena a lista arr usando o algoritmo de ordenação por seleção. """
    n = len(lista)
    for i in range(n):
        # encontrar o menor elemento na parte não ordenada
        indice_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        # trocar o menor elemento encontrado com o primeiro elemento não ordenado
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

def calcular_pastas(tamanhos, B):
    ordenar_selecao(tamanhos)  # ordenar os tamanhos dos arquivos usando Ordenação por Seleção
    i = 0  # menor arquivo: ponteiro
    j = len(tamanhos) - 1  # maior arquivo: ponteiro
    pastas = 0

    while i <= j:
        if tamanhos[i] + tamanhos[j] <= B:
            i += 1  # usa o menor arquivo
        # o maior arquivo é sempre usado aqui
        j -= 1
        pastas += 1  # atualizar a pasta

    return pastas

# entrada
N, B = map(int, input().split())
tamanhos = list(map(int, input().split()))

# inicio do problema
resultado = calcular_pastas(tamanhos, B)
print(resultado)
