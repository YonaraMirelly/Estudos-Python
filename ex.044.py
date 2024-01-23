print('=' * 10, end='')
print('LOJAS MARILENE', end='')
print('=' * 10)
preço = float(input('Preço das compras. R$'))
print('FORMAS DE PAGAMENTO')
print('[1] À vista dinheiro/cheque')
print('[2] À vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    d = preço - (10 * preço)/100 
    print('Sua compra de {} vai custar R${:.2f} no final.'.format(preço, d))
elif opçao == 2:
    d1 = preço - (5 * preço)/100
    print('Sua opção de {} vai custar R${:.2f} no final.'.format(preço,d1))
elif opçao == 3:
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela ))
elif opçao == 4:
    total = preço + (20 * preço/100)
    totalparcela = int(input('Em quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f}, COM JUROS.'.format(totalparcela, parcela))
    print('Sua compra de R${} vai acabar custando R${:.2f} no final.'.format(preço, total))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
input()


