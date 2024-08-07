#ok
def selection_sort(lista):
    for j in range(len(lista)-1):
        min_index = j
        for i in range(j, len(lista)):
            if lista[i] < lista[min_index]:
                min_index = i

        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    return lista
print(selection_sort([3,2,1]))