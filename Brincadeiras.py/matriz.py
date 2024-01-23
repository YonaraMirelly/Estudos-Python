dimensao = int(input("Digite a Dimensão da Matriz: "))

matriz = []
for l in range(dimensao):
    novaLinha = []
    for c in range(dimensao):
        elemento=int(input(f"Digite um valor para [{l+1,c+1}]:"))
        novaLinha.append(elemento)

    matriz.append(novaLinha)

print('='*40)

for l in range(dimensao):
    for c in range(dimensao):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()