#ok
def particionar(arr, baixo, alto):
    pivo = arr[alto]  # O pivô é o último elemento
    i = baixo - 1     # Índice do menor elemento

    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort(arr, baixo, alto):
    if baixo < alto:
        pi = particionar(arr, baixo, alto)

        quicksort(arr, baixo, pi - 1)  # Ordena os elementos antes da partição
        quicksort(arr, pi + 1, alto)   # Ordena os elementos após a partição

# Exemplo de uso
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Array ordenado:", arr)
