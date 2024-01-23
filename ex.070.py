print('-'*30)
print('{:^30}'.format(' LOJA SUPER BARATÃO '))
print('-'*30)
totalg = pm1000 = menor = cont =0
mb = ' '
while True:
    nome = str(input('Nome do produto: '))
    p = float(input('Preço: R$'))
    totalg +=p
    cont += 1
    if p > 1000:
        pm1000 +=1
    if cont == 1 or p < menor:
        menor = p
        mb = nome
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra foi de R${totalg:.2f}.')
print(f'{pm1000} produtos custam mais de 1000 reais.')
print(f'O produto mais barato é {mb} que custa R${menor}.')
input()