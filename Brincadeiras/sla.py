qtde = int(input())
lista = []
for _ in range(qtde):
    numero = int(input())
    lista += [numero]

junto = ''.join(str(num) for num in lista)
dic = {}

for i in range(10):
    dic[str(i)] = 0

for digito in junto:
    dic[digito] +=1

for chave, valor in dic.items():
    print(f'{chave} - {valor}')