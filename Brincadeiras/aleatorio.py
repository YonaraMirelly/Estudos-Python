from random import randint
linha = int(input('linha= '))
coluna = int(input('coluna = '))
matriz = []
soma = 0
produto = 1
for l in range(linha):
    li = []
    for c in range(coluna):
        if l == c:
            n = randint(0,9)
            li += [n]
            soma += n
        n = randint(0, 9)
        li += [n]
    matriz += [li]

print('MATRIZ...')
for l in range(linha):
    for c in range(coluna):
        print(f'[{matriz[l][c]:2}]', end = '')
    print()

print(f'SOMA DOS VALORES DA DIAGONAL PRINCIPAL = {soma} ')
