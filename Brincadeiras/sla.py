qtde = int(input())
lista = []
for _ in range(qtde):
    numero = int(input())
    lista += [numero]

junto = int(''.join(str(num) for num in lista))
dic = {}
cont = 0
for i in range(0, 9):
    if i in junto:
        cont +=1
        dic[i] = cont

for chave, valor in dic:
    print('f{chave} - {valor}')