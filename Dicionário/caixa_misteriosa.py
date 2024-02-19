print('Caixa misteriosa')

caixa = {}
for i in range(4):
    n = str(input("insira: "))
    caixa[i+1] = n

num = int(input('Diga um numero: '))
posi = caixa[num]
print(f'O(a) {posi} está inserida na posição {num}')