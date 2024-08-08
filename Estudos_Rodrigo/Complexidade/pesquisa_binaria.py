def pesquisa(lista, primeiro, ultimo, valor):
    if ultimo >= primeiro:
        indice_meio = (primeiro + ultimo) //2
        elemento_meio = lista[indice_meio]
        if elemento_meio == valor:
            return f'Encontrado na posição {indice_meio}'
        elif elemento_meio > valor:
            nova_posição = indice_meio -1
            return pesquisa(lista, primeiro, nova_posição, valor)
        elif elemento_meio < valor:
            nova_posição = indice_meio +1
            return pesquisa(lista, nova_posição, ultimo, valor) 
        else:
            return 'Não aparece na lista' 
        
print(pesquisa([1,2,7,4], 0, 3, 7))