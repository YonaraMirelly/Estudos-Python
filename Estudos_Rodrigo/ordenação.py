def main(lista, i = 0):
    if i == len(lista) -1:
        return lista
    else:
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            return main(lista)
    return main(lista, i+1)
    

if __name__ == "__main__":
    n = int(input())
    lista = [int(i) for i in input().split()]
    main(lista)
    print(*lista, end='')
