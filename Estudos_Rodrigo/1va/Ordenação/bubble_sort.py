#ok
def bubble_sort(lista):
    tamanho = len(lista)
    for j in range(tamanho-1):
        for i in range(tamanho-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

print(bubble_sort([3,2,1]))