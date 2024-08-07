#ok
def merge_sort(v): # receber uma lista como entrada
    inv = 0 # qtde de inversões
    if len(v) == 1: # caso base, se a lista só tem um elemento, retorno ela mesma
        return 0
    mid = len(v) // 2 # divisão da lista em duas metades = a e b
    a = v[:mid] # do início até a metada
    b = v[mid:] # da metade até o fim
    inv += merge_sort(a) # chama a recursão para armazenar as inversões retornadas
    inv += merge_sort(b)
    a += [float('inf')] # pra simplificar a lógica
    b += [float('inf')]
    ini1, ini2 = 0, 0
    for i in range(len(v)):
        if a[ini1] <= b[ini2]: # menor elemento
            v[i] = a[ini1]
            ini1 += 1
        else:
            v[i] = b[ini2] # significa que há inversões
            ini2 += 1
            inv += len(a) - ini1 - 1
    return inv
# entradas
def main():
    n = int(input())
    c = list(map(int, input().split()))
    print(merge_sort(c))
if __name__ == "__main__":
    main()
