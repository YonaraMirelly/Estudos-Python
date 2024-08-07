#ok
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontra o ponto do meio da lista
        L = arr[:mid]        # Divide a lista em duas metades
        R = arr[mid:]
        merge_sort(L)        # Ordena a primeira metade
        merge_sort(R)        # Ordena a segunda metade
        i = j = k = 0
        # Copia os dados para as listas L e R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Verifica se faltou algum elemento
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Array ordenado:", sorted_arr)
