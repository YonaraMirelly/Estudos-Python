def pificar(array, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and array[esq] > array[i]:
        maior = esq
    if dir < n and array[dir] > array[maior]:
        maior = dir
    
    if maior != i:
        array[i], array[maior] = array[maior], array[i]
        pificar(array, n, maior)

def heap(array):
    n = len(array)
    for i in range(n//2-1, -1,-1):
        pificar(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        pificar(array, i, 0)
    return array
print(heap([1,5,4,3,2]))