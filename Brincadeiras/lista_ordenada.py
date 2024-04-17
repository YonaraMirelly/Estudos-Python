lista_ordenada = [int(i) for i in input('lista -> ').split()]
print(f'Lista ordenada -> {lista_ordenada}')
maior = menor = lista_ordenada[0]
for j in lista_ordenada:
    if j > maior:
        maior = j
    elif j < menor:
        menor = j
print(f"Maior número na lista -> {maior}")
print(f"Menor número na lista -> {menor}")