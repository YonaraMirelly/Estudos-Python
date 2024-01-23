matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = []
impar = []
parsoma =  somaco3 = maior =0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] %2 ==0:
            par.append(matriz[l][c])
            parsoma += matriz[l][c]
        else:
            impar.append(matriz[l][c])
print('='*40)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print(f'Os valores pares digitados foram: {par} e a soma deles vale: {parsoma}!')
print(f'Os valores ímpares digitados foram: {impar}')
for l in range(0,3):
    somaco3 += matriz[l][2]
print(f'A soma de todos os valores da coluna 3 vale: {somaco3}!')
for c in range(0,3):
    if c ==0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2ª linha é {maior}')
input()