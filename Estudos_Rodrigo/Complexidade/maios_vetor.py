def maior(lista, i=0):
    if i == len(lista)-1:
        return lista[i]
    maior_atual = maior(lista, i+1)
    if lista[i] > maior_atual:
        maior_atual = lista[i]
    return maior_atual

print(maior([4,2,5,10]))