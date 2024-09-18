def marcação_de_regua(inicio, fim, altura, marcas):
    if altura == 0:
        return 
    else:
        meio = (inicio+fim)//2
        marcas[meio] = '-' * altura
        marcação_de_regua(inicio, meio, altura-1, marcas)
        marcação_de_regua(meio, fim, altura-1, marcas)

N, H = [int(x) for x in input().split()]
marcas = [' ' for _ in range(N+1)]
marcação_de_regua(0, N, H, marcas)

for i in range(N+1):
    print(f' {i}{marcas[i]} ')

