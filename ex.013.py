preço = float(input('Qual o salário do funcionário? R$'))
porcent = (preço * 15)/100
aumento = preço + porcent
print('Um funcionário que ganhava R$\033[1;31m{}\033[m, com 15% de aumento passará, a ganhar R$\033[1;32m{:.2f}\033[m.'.format(preço, aumento))
input()