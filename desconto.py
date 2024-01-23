preço = float(input('Digite o preço do produto: '))
porcent = (preço * 5)/100
desconto = (preço - porcent)
print('O produto que custava \033[1;31m{}\033[m, na promoção de 5%, custará R$\033[1;32m{:.2f}\033[m.'.format(preço, desconto))
input()