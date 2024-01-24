pessoas = []
dados = []
menor = maior = 0
escolha = 'Ss'
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    if escolha in 'Nn':
        break
print('='*40)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end= '')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}. Peso de ', end = '')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end = '')
input()