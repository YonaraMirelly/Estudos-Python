#ok
def heapificar(arr, n, i):
    maior = i      # Inicializa o maior como a raiz
    esq = 2 * i + 1  # Filho à esquerda
    dir = 2 * i + 2  # Filho à direita
    # Verifica se o filho à esquerda do nó existe e se é maior que a raiz
    if esq < n and arr[i] < arr[esq]:
        maior = esq
    # Verifica se o filho à direita do nó existe e se é maior que a raiz
    if dir < n and arr[maior] < arr[dir]:
        maior = dir
    # Troca a raiz se necessário
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        # Heapifica a raiz
        heapificar(arr, n, maior)
def heap_sort(arr):
    n = len(arr)
    # Constrói um max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapificar(arr, n, i)
    # Extrai elementos do heap um por um
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca o elemento atual com a raiz
        heapificar(arr, i, 0)            # Heapifica a raiz
# Exemplo de uso
arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print("Array ordenado:", arr)
